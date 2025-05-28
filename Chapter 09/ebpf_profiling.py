import os
import sys
import ctypes as ct
from bcc import BPF

bpf_code = """
#include <uapi/linux/ptrace.h>

BPF_PERF_OUTPUT(events);

struct event_t {
    u64 start_ts;
    u64 end_ts;
    u64 latency;
};

int measure_latency(struct pt_regs *ctx) {
    u64 start_ts = bpf_ktime_get_ns();
    u64 pid = bpf_get_current_pid_tgid();
    
    u64 end_ts = bpf_ktime_get_ns();
    u64 latency = end_ts - start_ts;
    
    struct event_t event = {
        .start_ts = start_ts,
        .end_ts = end_ts,
        .latency = latency,
    };
    events.perf_submit(ctx, &event, sizeof(event));
    return 0;
}
"""
bpf = BPF(text=bpf_code)

# Attach eBPF program to syscalls of interest
bpf.attach_kprobe(event=bpf.get_syscall_fnname("getpid"), fn_name="measure_latency")

# Define output handler
def print_event(cpu, data, size):
    class PerfEvent(ct.Structure):
        _fields_ = [("start_ts", ct.c_ulonglong),
                    ("end_ts", ct.c_ulonglong),
                    ("latency", ct.c_ulonglong)]

    event = ct.cast(data, ct.POINTER(PerfEvent)).contents
    print(f"Latency: {event.latency / 1e6} milliseconds")

# Output handler callback
bpf["events"].open_perf_buffer(print_event)

# Main loop
while True:
    try:
        bpf.perf_buffer_poll()
    except KeyboardInterrupt:
        sys.exit()

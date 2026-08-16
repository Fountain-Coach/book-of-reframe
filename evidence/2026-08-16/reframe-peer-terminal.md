# Reframe-to-Reframe MIDI2 peer terminal acceptance

Scenario: `reframe-to-reframe-peer-projection`  
Status: live-accepted for software-peer acceptance  
Runtime source: `Fountain-Coach/midi2-gpu-fabric@cbf31bdb`  
Evidence date: 2026-08-16

The independent witness drove a separate Reframe software peer against a fresh target Reframe process. The peer
requested the existing `storify.source.start` operation over the MIDI2 backplane. The target exposed writer consent,
then persisted the terminal Store lifecycle `requested → accepted → running → succeeded`; the peer received the
matching terminal MIDI2 event.

The target accessibility projection exposed `MIDI2 peers`, the target as `Admitted`, the software peer as `Completed`,
and the operation as `Completed · storify.source.start`. The matching window-ID capture is
[`reframe-peer-terminal-20260816.png`](reframe-peer-terminal-20260816.png).

This public record intentionally omits process IDs, Store paths, correlation identifiers, raw Store documents, and
manuscript material. Those belong to the maintainer evidence bundle. The claim is limited to software-peer acceptance;
no physical MIDI2 hardware interoperability is claimed.

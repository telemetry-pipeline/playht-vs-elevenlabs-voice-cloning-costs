#!/usr/bin/env python3
"""
PlayHT vs ElevenLabs Voice Cloning TCO & Seat Cost Calculator 2026.
"""
import argparse

def calculate(words, seats):
    chars = words * 5
    playht_base = 39.0 * seats
    playht_words = 250000 * seats
    playht_overage = max(0, words - playht_words) * 0.0002
    playht_total = playht_base + playht_overage

    eleven_base = 99.0 * seats
    eleven_chars = 500000 * seats
    eleven_overage = (max(0, chars - eleven_chars) / 1000.0) * 0.24
    eleven_total = eleven_base + eleven_overage

    diff = eleven_total - playht_total

    print("=" * 60)
    print("Voice Synthesis TCO: PlayHT vs ElevenLabs")
    print("=" * 60)
    print(f"Monthly Word Demand:     {words:,} words ({chars:,} chars)")
    print(f"Producer Seats:          {seats}")
    print(f"PlayHT Creator Monthly:  ${playht_total:.2f}/mo")
    print(f"ElevenLabs Pro Monthly:  ${eleven_total:.2f}/mo")
    print(f"Monthly Cost Difference: ${abs(diff):.2f}/mo ({'PlayHT Cheaper' if diff > 0 else 'ElevenLabs Cheaper'})")
    print("=" * 60)
    return playht_total, eleven_total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PlayHT vs ElevenLabs Calculator")
    parser.add_argument("--words", type=int, default=150000)
    parser.add_argument("--seats", type=int, default=2)
    args = parser.parse_args()
    calculate(args.words, args.seats)

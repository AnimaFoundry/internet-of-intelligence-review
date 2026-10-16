"""Original, illustrative arithmetic. No hardware or training measurements."""
from decimal import Decimal as D
import json
from pathlib import Path


def calculate():
    nodes, channels, bits, day = D(1000000), D(6), D(16), D(86400)
    rows = []
    for rate in [D('0.1'), D(1), D(10)]:
        raw = nodes * channels * bits / 8 * rate * day
        rows.append({'rate_hz': str(rate), 'raw_bytes_per_day': str(raw),
                     'raw_TB_per_day_decimal': str(raw / D(10)**12),
                     'ten_percent_payload_GB_per_day': str(raw * D('.1') / D(10)**9)})
    retained = nodes * day * D('.1')
    seconds = D(2) * retained / D(50000)
    update_bytes = D(1000000) * D(4) / 8
    e_receive = update_bytes * 8 * D('0.0000001')
    harvest_seconds = e_receive / D('0.00001')
    return {
        'status': 'ILLUSTRATIVE_ASSUMPTIONS_NOT_MEASUREMENTS',
        'assumptions': {'nodes': str(nodes), 'channels': str(channels),
            'bits_per_channel': str(bits), 'payload_retained_fraction': '0.1',
            'sample_retention_scenario': '10% of complete fixed-size joint records; no re-encoding',
            'recording_seconds': str(day), 'training_passes': '2',
            'hypothetical_training_samples_per_second': '50000',
            'update_parameters': '1000000', 'bits_per_parameter': '4',
            'hypothetical_receive_joules_per_bit': '0.0000001',
            'hypothetical_surplus_harvest_watts': '0.00001'},
        'traffic': rows,
        'one_hz_retained_joint_samples': str(retained),
        'hypothetical_training_seconds': str(seconds),
        'hypothetical_training_hours': str(seconds / 3600),
        'update_bytes_without_metadata': str(update_bytes),
        'receive_energy_joules_without_overheads': str(e_receive),
        'harvest_seconds_for_receive_only': str(harvest_seconds),
        'harvest_hours_for_receive_only': str(harvest_seconds / 3600),
        'fleet_unicast_payload_TB_decimal': str(update_bytes * nodes / D(10)**12),
        'not_included': ['headers', 'timestamps', 'loss/retransmissions', 'synchronization',
            'representation quality', 'preprocessing', 'training utilization variation',
            'model optimizer/memory', 'update verification', 'flash writes', 'rollback storage'],
    }


if __name__ == '__main__':
    result = calculate()
    destination = Path(__file__).resolve().parents[1] / 'budget_example.json'
    destination.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))

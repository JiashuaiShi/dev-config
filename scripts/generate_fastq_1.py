import random
import gzip
import argparse

"""
python generate_fastq_1.py --max_length 500 --num_reads 200 --output_filename "custom_fastq.fastq.gz"
"""

def generate_random_sequence(length):
    """生成指定长度的随机DNA序列"""
    return ''.join(random.choices('ACGT', k=length))

def generate_random_quality(length):
    """生成指定长度的随机质量分数"""
    return ''.join(chr(random.randint(33, 73)) for _ in range(length))

def generate_fastq_entry(seq_id, sequence, quality):
    """生成一个fastQ条目"""
    return f"@{seq_id}\n{sequence}\n+\n{quality}\n"

def generate_fastq(filename, num_reads, max_length=2048):
    """生成一个包含随机reads的fastQ文件"""
    with gzip.open(filename, 'wt') as f:
        for i in range(num_reads):
            seq_length = random.randint(50, max_length)  # 生成1到max_length之间的随机长度
            sequence = generate_random_sequence(seq_length)
            quality = generate_random_quality(seq_length)
            assert len(sequence) == len(quality), "Sequence and quality lengths do not match"
            fastq_entry = generate_fastq_entry(f'read_{i}', sequence, quality)
            f.write(fastq_entry)

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="Generate a fastQ file with random sequences.")
    parser.add_argument('--max_length', type=int, default=2048, help='Maximum length of the DNA sequences.')
    parser.add_argument('--num_reads', type=int, default=1000, help='Number of reads to generate.')
    parser.add_argument('--output_filename', type=str, default='small_fastq.fastq.gz', help='Output filename.')
    return parser.parse_args()

# 解析命令行参数
args = parse_args()

# 使用命令行参数
generate_fastq(args.output_filename, args.num_reads, args.max_length)
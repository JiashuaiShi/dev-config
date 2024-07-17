import random
import argparse

"""
python generate_fastq.py --read_length 100 --num_lines_k 10
python generate_fastq.py --read_length 100 --num_lines_k 10 --paired_end
"""

def generate_random_dna_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def generate_fastq(read_length, num_lines_k=1, paired_end=False):
    num_reads = num_lines_k * 250  # 每个read包含4行，因此每1000行有250个reads

    if paired_end:
        with open('output_1.fastq', 'w') as f1, open('output_2.fastq', 'w') as f2:
            for i in range(num_reads):
                sequence_id = f"@SEQ_ID_{i}"
                sequence = generate_random_dna_sequence(read_length)
                plus_line = "+"
                quality_scores = ''.join(random.choice('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJ') for _ in range(read_length))
                
                f1.write(f"{sequence_id}/1\n{sequence}\n{plus_line}\n{quality_scores}\n")
                
                sequence_pe = generate_random_dna_sequence(read_length)
                quality_scores_pe = ''.join(random.choice('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJ') for _ in range(read_length))
                
                f2.write(f"{sequence_id}/2\n{sequence_pe}\n{plus_line}\n{quality_scores_pe}\n")
    else:
        with open('output.fastq', 'w') as f:
            for i in range(num_reads):
                sequence_id = f"@SEQ_ID_{i}"
                sequence = generate_random_dna_sequence(read_length)
                plus_line = "+"
                quality_scores = ''.join(random.choice('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJ') for _ in range(read_length))
                
                f.write(f"{sequence_id}\n{sequence}\n{plus_line}\n{quality_scores}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a FastQ file with specified read length, number of lines, and type (SE or PE).",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--read_length", type=int, required=True, help="Length of the reads.")
    parser.add_argument("--num_lines_k", type=int, default=1, help="Number of lines in thousands (default is 1k lines).")
    parser.add_argument("--paired_end", action='store_true', help="Generate paired-end FastQ files if set; otherwise, single-end.")
    
    args = parser.parse_args()
    
    generate_fastq(args.read_length, args.num_lines_k, args.paired_end)

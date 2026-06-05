dataset = []
with open('/home/lakshay/RAG_Pipeline/Data/Text_files/text2.txt', 'r') as f:
    dataset = f.read().splitlines()
    print(f"Dataset loaded with {len(dataset)} entries.")
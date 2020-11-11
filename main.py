import os
from trans import back_translate


def extract_nlu(f):
	nlus = []
	for line in f:
		line = line.strip()
		if line:
			if line.startswith('## intent:'):
				intent = line.split()[-1]
				new_dict = {}
				new_dict[intent] = []
				current_intent = intent

			elif line.startswith('-'):
				line = line.replace(' ', '').replace('-', '')
				back_translated = back_translate(line)
				print(back_translated)
				if back_translated != line and back_translated not in new_dict[intent]:
					new_dict[intent].append(back_translated)
		else:
			nlus.append(new_dict)


	print(nlus)
	return nlus

origin = '/home/mlp/current/yixing-bot/data/'
nlu_files = [os.path.join(origin, f) for f in os.listdir(origin) if f.startswith('nlu')]

content_master = []
for nlu_file in nlu_files:
	with open(nlu_file) as f:
		content_master.extend(extract_nlu(f))
		f.close()
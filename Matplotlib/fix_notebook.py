import json

with open(r'c:\Users\Lenovo\Python_Library\Matplotlib\plotting_line.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        if 'Student Performance' in src:
            # Remove existing set_xlim line if present, then add it after autoscale
            new_source = []
            for line in cell['source']:
                if 'ax.set_xlim(1, 4)' in line:
                    continue  # skip old placement
                new_source.append(line)
                if 'ax.autoscale()' in line:
                    new_source.append("ax.set_xlim(1, 4)\n")
            cell['source'] = new_source
            print('Cell modified successfully!')
            break

with open(r'c:\Users\Lenovo\Python_Library\Matplotlib\plotting_line.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('File saved.')

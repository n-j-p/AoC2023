example_input='rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
testing = False
if testing:
    inp = example_input
else:
    inp = open('./day15_input.txt').read()[:-1]
def hash(astr):
    cur = 0
    for chr in astr:
        cur += ord(chr)
        cur *= 17
        cur = cur % 256
    return cur

c = 0
for x in inp.split(','):
    hx = hash(x)
    print(x, hx)

    c += hx

print('\n',c)

# --- Part 2 ---

def hashmap(steps, boxes = [[] for _ in range(256)]):
    for step in steps.split(','):
        if '-' in step:
            sep = '-'
        else: # or '+' in step
            sep = '='
        step_split = step.split(sep)
        if sep == '=':
            foclen = int(step_split[1])
        else:
            foclen = None
        label = step_split[0]
        box = hash(label)
        if label in [x[0] for x in boxes[box]]:
            print('present')
            if sep == '-':
                print('removing lens',label)
                ix = [x[0] for x in boxes[box]].index(label)
                boxes[box].pop(ix)
            else:
                print('changing lens',label)
                ix = [x[0] for x in boxes[box]].index(label)
                boxes[box][ix][1] = foclen
                
        else:
            print('not present')
            if foclen is not None:
                boxes[box].append([label, foclen])
    return boxes

def score(boxes):
    ctot = 0
    for i,x in enumerate(boxes):
        a = i + 1
        for j, y in enumerate(x):
            b = j + 1
            c = y[1]
            print(f'- {y[0]}: {a} (box {i}) * {b} * {c} = {a*b*c}')
            ctot += a*b*c
    return ctot

boxes = hashmap(inp)
print("\n",score(boxes))

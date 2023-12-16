def reflections(mirror):
    size = len(mirror)

    for i in range(size - 1):
        step = 0

        while i - step >= 0 and i + step + 1 < size:
            if mirror[i - step] != mirror[i + step + 1]:
                break
            step += 1
        else:
            return i + 1

    return 0


with open('input.txt') as file:
    mirrors = file.read().split('\n\n')

mirrors = [mirror.splitlines() for mirror in mirrors]
print(sum(reflections(m) * 100 + reflections(list(zip(*m))) for m in mirrors))

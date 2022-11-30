import ast

def survivor(terms):
    rest = list(t for t in terms[::2])
    if ( len(terms) % 2 ): rest.pop(0)
    if len(rest) > 1: return survivor(rest)
    return rest[0]

def main():
    mecenas = open('mecenas.json')
    mecenas = [{'name': m, 'pos': ix} for ix,m in enumerate(ast.literal_eval(mecenas.read()))]
    
    rest = survivor(mecenas)
    print(f'{rest["name"]}-{rest["pos"]}')

if __name__ == '__main__':
    main()
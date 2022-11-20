
import ast

def bestSerie(colors):
    maxSerie = []
    currentSerie = []
    for color in colors:
        currentLen = len(currentSerie)
        if  (currentLen > 0 and color == currentSerie[-1]) or (currentLen > 1 and color != currentSerie[-2]):
            
            # restart serie with previous and new color
            currentSerie = [currentSerie[-1],color]
        else:
             currentSerie.append(color)
             maxSerie = currentSerie if len(currentSerie) > len(maxSerie) else maxSerie

    return maxSerie

def main():
    file = open('colors.txt')
    colors = ast.literal_eval(file.read())
    serie = bestSerie(colors)

    print(serie)
    print(f'{len(serie)}@'+serie[-1] )


if __name__ == '__main__':
    main()
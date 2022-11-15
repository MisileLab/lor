class InputOutput:
    def __init__(self, input: str, output: str):
        self.input = input
        self.output = output

def get_input_and_output(n: str | int) -> InputOutput:
    if isinstance(n, str):
        n = int(n)
    a = {
        8723: InputOutput("3 4 5", "1"),
        8558: InputOutput("4", "4"),
        6778: InputOutput("2\n3", "VladSaturnian\nGraemeMercurian"),
        5893: InputOutput("10110111", "110000100111"),
        5543: InputOutput("800\n700\n900\n198\n330", "848"),
        4696: InputOutput("7\n1\n2.5\n0", "2801.00\n5.00\n64.44"),
        2752: InputOutput("3 1 2", "1 2 3"),
        21598: InputOutput("2", "SciComLove\nSciComLove"),
        15680: InputOutput("0", "YONSEI"),
        15000: InputOutput("canyoupickupsomegroceries", "CANYOUPICKUPSOMEGROCERIES"),
        14581: InputOutput("h0ngjun7", ":fan::fan::fan:\n:fan::h0ngjun7::fan:\n:fan::fan::fan:"),
        14173: InputOutput("6 6 8 8\n1 8 4 9", "49"),
        13866: InputOutput("4 7 10 20", "7"),
        13496: InputOutput("2\n3 20 31\n42 70\n1000 2000\n512 121\n3 10 3\n29 1\n30 2\n31 4", "Data Set 1:\n191\n\nData Set 2:\n3"),
        11945: InputOutput("5 7\n0010000\n0111010\n1111111\n0111010\n0010000", "0000100\n0101110\n1111111\n0101110\n0000100"),
        11365: InputOutput("!edoc doog a tahW\nnoitacitsufbo\nerafraw enirambus detcirtsernu yraurbeF fo tsrif eht no nigeb ot dnetni eW\nlla sees rodroM fo drol eht ,ssertrof sih nihtiw delaecnoC\nEND",
                           "What a good code!\nobfustication\nWe intend to begin on the first of February unrestricted submarine warfare\nConcealed within his fortress, the lord of Mordor sees all"),
        10817: InputOutput("20 30 10", "20"),
        10156: InputOutput("250 2 140", "360"),
        8718: InputOutput("10 2", "7000"),
        7891: InputOutput("4\n-100 100\n2 3\n0 110101\n-1000000000 1", "0\n512\n110101\n-999999999"),
        6764: InputOutput("1\n10\n12\n13", "Fish Rising"),
        5717: InputOutput("2 2\n2 3\n5 5\n1 1\n0 0", "4\n5\n10\n2"),
        5532: InputOutput("15\n32\n48\n4\n6", "7"),
        4589: InputOutput("3\n40 62 77\n88 62 77\n91 33 18", "Gnomes:\nOrdered\nUnordered\nOrdered"),
        2742: InputOutput("5", "5\n4\n3\n2\n1"),
        18409: InputOutput("6\nbitaro", "4"),
        15552: InputOutput("5\n1 1\n12 34\n5 500\n40 60\n1000 1000", "2\n46\n505\n100\n2000"),
        15726: InputOutput("32 16 8", "64"),
        15873: InputOutput("102", "12"),
        18409: InputOutput("8\njoiyosen", "4"),
        21598: InputOutput("2", "SciComLove\nSciComLove"),
        23235: InputOutput("5 21 44 48 48 64\n6 8 19 22 49 53 62\n8 5 9 14 17 24 25 27 61\n4 13 21 28 35\n5 31 38 44 49 60\n0",
        "Case 1: Sorting... done!\nCase 2: Sorting... done!\nCase 3: Sorting... done!\nCase 4: Sorting... done!\nCase 5: Sorting... done!"),
        4714: InputOutput("100.0\n12.0\n0.12\n120000.0\n-1.0", "Objects weighing 100.00 on Earth will weigh 16.70 on the moon.\nObjects weighing 12.00 on Earth will weigh 2.00 on the moon.\nObjects weighing 0.12 on Earth will weigh 0.02 on the moon.\nObjects weighing 120000.00 on Earth will weigh 20040.00 on the moon.")
    }
    return a[n]

import copy
import json
import data
import xlsxwriter

from core import calc_all, rank

if __name__ == "__main__":
    result = calc_all()

    filterResults = list(
        filter(lambda r: r["G1W"]["name"] == "NIP" and r["G2W"]["name"] == "FPX" and r["G3W"]['name'] == "NIP",
               result))
    ranks = list(map(rank, filterResults))

    dumps = []

    with open("result.json", "w+") as f:
        for rank in ranks:
            for index, team in rank.items():
                team['playoff'] = data.summerFinalRankScoreMap[index]
                team['total'] = team['playoff'] + team['spring']
            rank = sorted(list(rank.values()), key=lambda x: (x['total'], x['playoff']), reverse=False)
            rank = list(
                map(lambda x: x['name']
                    , rank[-6:]
                    )
            )

            oneTwoThree = set(rank[-3:])
            if oneTwoThree != {"TES", "LNG", "BLG"} or "AL" in rank:
                continue

            dumps.append(rank)
        dumps = list(map(list, map(reversed, dumps)))
        f.write(json.dumps(dumps, indent=4))

        workbook = xlsxwriter.Workbook('./result.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0

        for col, data in enumerate(dumps):
            worksheet.write_column(row, col, data)

        workbook.close()

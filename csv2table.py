# -*- coding: utf-8 -*-
import csv

isFirst = True
with open('Book1.csv', "r", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=",", quotechar='"')

    with open('table.html', 'w', encoding='utf-8') as htmlfile:
        print('<table style="width: 100%; border: solid 1px #ffffff">', file=htmlfile)
        for row in rows:
            row_length = len(row)
            if isFirst == True:
                print('    <thead>', file=htmlfile)
                print('        <tr>', file=htmlfile)
                for col in row:
                    print('            <th>{0}</th>'.format(col.replace("\n", "<br/>")), file=htmlfile)
                print('        </tr>', file=htmlfile)
                print('    </thead>', file=htmlfile)
                print('    <tbody>', file=htmlfile)
                isFirst = False
            else:
                print('        <tr>', file=htmlfile)
                for col in row:
                    print('            <td>{0}</td>'.format(col.replace("\n", "<br/>")), file=htmlfile)
                print('        </tr>', file=htmlfile)
        print('    </tbody>', file=htmlfile)
        print('</table>', file=htmlfile)
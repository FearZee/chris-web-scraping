import xlsxwriter

workbook = xlsxwriter.Workbook(f'Premiere League.xlsx')
def create_excel(data, name='data', wb_name=''):
    workbook = xlsxwriter.Workbook(f'{name}-{wb_name}.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column(1, 1, 15)
    worksheet.set_column(1, 0, 15)
    worksheet.set_column(1, 21, 15)
    worksheet.set_column(1, 22, 15)

    worksheet.write('A1', 'Home Team')
    worksheet.write('B1', 'Away Team')
    worksheet.write('C1', 'H Fouls')
    worksheet.write('D1', 'A Fouls')
    worksheet.write('E1', 'H Touches')
    worksheet.write('F1', 'A Touches')
    worksheet.write('G1', 'H Tackles')
    worksheet.write('H1', 'A Tackles')
    worksheet.write('I1', 'H Interceptions')
    worksheet.write('J1', 'A Interceptions')
    worksheet.write('K1', 'H Aerials Won')
    worksheet.write('L1', 'A Aerials Won')
    worksheet.write('M1', 'H Clearances')
    worksheet.write('N1', 'A Clearances')
    worksheet.write('O1', 'H Gelb')
    worksheet.write('P1', 'A Gelb')
    worksheet.write('Q1', 'H GelbRot')
    worksheet.write('R1', 'A GelbRot')
    worksheet.write('S1', 'H Rot')
    worksheet.write('T1', 'A Rot')
    worksheet.write('U1', 'H Possession (in per cent)')
    worksheet.write('V1', 'A Possession (in per cent)')
    worksheet.write('W1', 'H Shots on Target')
    worksheet.write('X1', 'A Shots on Target')

    write_data(worksheet, data)
    workbook.close()



def write_data(worksheet, data):
    row = 1
    col = 0

    for home_team, away_team, h_fouls, a_fouls, h_touches, a_touches, h_tackles, a_tackles, h_interceptions, a_interceptions, h_aerials_won, a_aerials_won, h_clearances, a_clearances, h_yellow_cards,a_yellow_cards, h_yellow_red_cards, a_yellow_red_cards, h_red_cards, a_red_cards, h_possession,a_possession, h_shots_on_target, a_shots_on_target in (data):
        worksheet.write_string(row, col, home_team)
        worksheet.write_string(row, col + 1, away_team)
        worksheet.write_number(row, col + 2, int(h_fouls))
        worksheet.write_number(row, col + 3, int(a_fouls))
        worksheet.write_number(row, col + 4, int(h_touches))
        worksheet.write_number(row, col + 5, int(a_touches))
        worksheet.write_number(row, col + 6, int(h_tackles))
        worksheet.write_number(row, col + 7, int(a_tackles))
        worksheet.write_number(row, col + 8, int(h_interceptions))
        worksheet.write_number(row, col + 9, int(a_interceptions))
        worksheet.write_number(row, col + 10, int(h_aerials_won))
        worksheet.write_number(row, col + 11, int(a_aerials_won))
        worksheet.write_number(row, col + 12, int(h_clearances))
        worksheet.write_number(row, col + 13, int(a_clearances))
        worksheet.write_number(row, col + 14, len(h_yellow_cards))
        worksheet.write_number(row, col + 15, len(a_yellow_cards))
        worksheet.write_number(row, col + 16, len(h_yellow_red_cards))
        worksheet.write_number(row, col + 17, len(a_yellow_red_cards))
        worksheet.write_number(row, col + 18, len(h_red_cards))
        worksheet.write_number(row, col + 19, len(a_red_cards))
        worksheet.write_number(row, col + 20, int(h_possession[:-1]))
        worksheet.write_number(row, col + 21, int(a_possession[:-1]))
        worksheet.write_number(row, col + 22, int(h_shots_on_target.split()[0]))
        worksheet.write_number(row, col + 23, int(a_shots_on_target.split()[2]))
        row += 1

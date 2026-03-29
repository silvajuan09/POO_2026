class EntradaCinema:
    def __init__ (self):
        self.dia = input('Digite o dia: ')
        self.horario = float(input('Digite o horário: '))
    def calc_entrada(self):
        match self.dia:
            case 'Segunda': ing = 16
            case 'Terça': ing = 16
            case 'Quarta': ing = 8
            case 'Quinta': ing = 16
            case 'Sexta': ing = 20
            case 'Sábado': ing = 20
            case 'Domingo': ing = 20
            case _: print('Dia inválido!')
        if 17 <= self.horario <= 24:
            ing = ing + ing/2
        return ing

cinema = EntradaCinema()
cinema.ingresso = cinema.calc_entrada()
print(f'O valor do ingresso é de R${cinema.ingresso}')
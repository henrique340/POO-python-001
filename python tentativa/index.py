class cadastro:

    def __init__(self, nome, idade, notas):
        '''
        ---> método init
        :param nome: indica nome no PP
        :param idade: indica idade no PP
        :param notas: indica notas no PP
        '''
        self.nome=nome
        self.idade=idade
        self.notas=notas

    def ver_notas(self):
        '''
        --> método ver as notas
        :return: notas
        '''
        return self.notas


class curso:

    def __init__(self, nome_curso, max_alunos):
        '''
        ---> método init
        :param nome_curso: indicar o nome do curso no PP
        :param max_alunos: indicar o n° max de alunos no PP
        '''
        self.nome_curso=nome_curso
        self.max_alunos=max_alunos
        self.alunos_lista = []

    def add_estudante(self, estudante):
        '''
        ---> método para adicionar um aluno
        :param estudante: informações do cadastro
        :return: valor das informações
        '''
        if len(self.alunos_lista) < self.max_alunos:
            self.alunos_lista.append(estudante)
            return estudante
        return False

    def media_notas(self):
        '''
        --->método média
        :return: média dos alunos
        '''
        valor = 0
        for e in self.alunos_lista:
            valor += e.ver_notas()
        return valor/len(self.alunos_lista)


#programa principal - cadastrar
s1 = cadastro('Yuji', 16, 6.5)
s2 = cadastro('Billy', 17, 9.5)

course = curso('grupo_de_estudos', 2)

course.add_estudante(s1)
course.add_estudante(s2)
print('-' * 45)
print(f'{course.nome_curso:^45}')
print('-' * 45)
print(f'\t\to aluno 1 se chama: {course.alunos_lista[0].nome} e tirou {s1.ver_notas()}')
print(f'\t\to aluno 2 se chama: {course.alunos_lista[1].nome} e tirou {s2.ver_notas()}')
print(f'\t\ta média dos alunos é {course.media_notas()}')

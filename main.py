# coding: utf-8

from abc import ABC, abstractmethod


class Department:
    """
    Classe base Departmante

    :param name: Nome do departamento
    :param code: Código do departamento
    """
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    """
    Classe base Employee

    :param code: Código do empregado
    :param name: Nome do empregado
    :param salary: Salário do empregado
    :param department: Departamento ao que o empregado pertence
    """
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    def get_departament(self):
        """
        Retorna o nome do atual departamento do empregado

        :return: Nome do departamento do empregado
        """
        return self.__department.name

    def set_department(self, department_name):
        """
        Modifica o nome do atual departamento do empregado

        :param department_name: Novo nome para o departakmento
        """
        self.__department.name = department_name

    @abstractmethod
    def calc_bonus(self):
        """
        Método abstrato para calculo de bônus salarial do funcionário
        """
        pass

    def get_hours(self):
        """
        Retorna a jornada de trabalho. Por padrão é definida como 8 horas

        :return: Carga horária
        """
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
	# Inicia com os dados na superclasse
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15  # Bônus de 15% salarial


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2)) 
        self.__sales = 0

    def get_sales(self):
        """
        Obtém o valor total das vendas do funcionário

        :return: Valor de vendas
        """
        return self.__sales

    def put_sales(self, sale):
        """
        Incrementa o total de vendas com uma nova venda

        :param sale: Valor da nova venda
        """
        self.__sales += sale

    def calc_bonus(self):
        return self.__sales * 0.15  # Bônus de 15% sobre as vendas

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Função para gerar compisições com os valores fornecidos em uma lista.
def gerarSubListasRecursiva(listaEntrada, listaInicial=None):
    
    #iniciando a lista inicial com valor(es) passado(s) ou lista vazia []
    listaInicial = listaInicial or []

    #Salva o estado da listaInicial que será usado nas iterações
    yield listaInicial

    #Caso base para o retorno caso a lista seja vazia...
    if len(listaEntrada) == 0:
        return

    #Laço de iteração quando a lista não for vazia...
    for i, sublista in enumerate(listaEntrada):
        for listaRetornada in gerarSubListasRecursiva(listaEntrada[i + 1:], listaInicial + [sublista]):
            yield listaRetornada
# Given an array of currencies, find out if a net positive gain can be made by traversing through all esges of the graph

import math
def detectArbitrage(exchangeRates):
    logExchangeRates = convertToLogMatrix(exchangeRates)
	return foundNegativeWeightCycle(logExchangeRates,0)

def foundNegativeWeightCycle(graph,start):
	distanceFromStart = [float('inf') for _ in range(len(graph))]
	distanceFromStart[start] = 0
	
	for _ in range(len(graph)-1):
		if not relaxEdges(graph,distanceFromStart):
			return False
	
	return relaxEdges(graph,distanceFromStart)

def relaxEdges(graph,distances):
	updated = False
	
	for sourceIdx, edges in enumerate(graph):
		for destinationIdx, edgeWeight in enumerate(edges):
			newDistance = distances[sourceIdx] + edgeWeight
			if newDistance < distances[destinationIdx]:
				updated = True
				distances[destinationIdx] = newDistance
	return updated

def convertToLogMatrix(matrix):
	newMatrix = []
	for row, rates in enumerate(matrix):
		newMatrix.append([])
		for rate in rates:
			newMatrix[row].append(-math.log10(rate))
	
	return newMatrix

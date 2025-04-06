using System;
using System.Collections.Generic;

// Clase Nodo
class Nodo
{
    public string Nombre { get; set; }
    public List<Nodo> Conexiones { get; set; }

    // Constructor
    public Nodo(string nombre)
    {
        Nombre = nombre;
        Conexiones = new List<Nodo>();
    }

    // Método para conectar nodos
    public void Conectar(Nodo nodo)
    {
        Conexiones.Add(nodo);
    }
}

// Clase Grafo
class Grafo
{
    public List<Nodo> Nodos { get; set; }

    // Constructor
    public Grafo()
    {
        Nodos = new List<Nodo>();
    }

    // Método para agregar nodos al grafo
    public void AgregarNodo(Nodo nodo)
    {
        Nodos.Add(nodo);
    }

    // Método para mostrar el grafo
    public void MostrarGrafo()
    {
        foreach (var nodo in Nodos)
        {
            Console.WriteLine($"Nodo {nodo.Nombre}:");
            foreach (var conexion in nodo.Conexiones)
            {
                Console.WriteLine($"  -> {conexion.Nombre}");
            }
        }
    }
}

class Program
{
    static void Main()
    {
        // Crear nodos
        Nodo nodoA = new Nodo("A");
        Nodo nodoB = new Nodo("B");
        Nodo nodoC = new Nodo("C");

        // Conectar nodos
        nodoA.Conectar(nodoB);
        nodoB.Conectar(nodoC);
        nodoC.Conectar(nodoA);  // Grafo no dirigido

        // Crear el grafo y agregar nodos
        Grafo grafo = new Grafo();
        grafo.AgregarNodo(nodoA);
        grafo.AgregarNodo(nodoB);
        grafo.AgregarNodo(nodoC);

        // Mostrar la representación del grafo
        grafo.MostrarGrafo();
    }
}

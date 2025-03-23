// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
using System;

class Nodo
{
    public int valor;
    public Nodo izquierdo, derecho;

    public Nodo(int valor)
    {
        this.valor = valor;
        izquierdo = derecho = null;
    }
}

class ArbolBinario
{
    public Nodo raiz;

    public ArbolBinario()
    {
        raiz = null;
    }

    // Insertar un nodo
    public void Insertar(int valor)
    {
        raiz = InsertarRecursivo(raiz, valor);
    }

    private Nodo InsertarRecursivo(Nodo raiz, int valor)
    {
        if (raiz == null)
        {
            raiz = new Nodo(valor);
            return raiz;
        }

        if (valor < raiz.valor)
            raiz.izquierdo = InsertarRecursivo(raiz.izquierdo, valor);
        else if (valor > raiz.valor)
            raiz.derecho = InsertarRecursivo(raiz.derecho, valor);

        return raiz;
    }

    // Recorrido en inorden
    public void RecorridoInorden()
    {
        RecorridoInordenRecursivo(raiz);
    }

    private void RecorridoInordenRecursivo(Nodo raiz)
    {
        if (raiz != null)
        {
            RecorridoInordenRecursivo(raiz.izquierdo);
            Console.Write(raiz.valor + " ");
            RecorridoInordenRecursivo(raiz.derecho);
        }
    }

    // Recorrido en preorden
    public void RecorridoPreorden()
    {
        RecorridoPreordenRecursivo(raiz);
    }

    private void RecorridoPreordenRecursivo(Nodo raiz)
    {
        if (raiz != null)
        {
            Console.Write(raiz.valor + " ");
            RecorridoPreordenRecursivo(raiz.izquierdo);
            RecorridoPreordenRecursivo(raiz.derecho);
        }
    }

    // Recorrido en postorden
    public void RecorridoPostorden()
    {
        RecorridoPostordenRecursivo(raiz);
    }

    private void RecorridoPostordenRecursivo(Nodo raiz)
    {
        if (raiz != null)
        {
            RecorridoPostordenRecursivo(raiz.izquierdo);
            RecorridoPostordenRecursivo(raiz.derecho);
            Console.Write(raiz.valor + " ");
        }
    }

    // Búsqueda de un valor
    public bool Buscar(int valor)
    {
        return BuscarRecursivo(raiz, valor) != null;
    }

    private Nodo BuscarRecursivo(Nodo raiz, int valor)
    {
        if (raiz == null || raiz.valor == valor)
            return raiz;

        if (valor < raiz.valor)
            return BuscarRecursivo(raiz.izquierdo, valor);

        return BuscarRecursivo(raiz.derecho, valor);
    }

    // Eliminar un nodo
    public void Eliminar(int valor)
    {
        raiz = EliminarRecursivo(raiz, valor);
    }

    private Nodo EliminarRecursivo(Nodo raiz, int valor)
    {
        if (raiz == null)
            return raiz;

        if (valor < raiz.valor)
            raiz.izquierdo = EliminarRecursivo(raiz.izquierdo, valor);
        else if (valor > raiz.valor)
            raiz.derecho = EliminarRecursivo(raiz.derecho, valor);
        else
        {
            if (raiz.izquierdo == null)
                return raiz.derecho;
            else if (raiz.derecho == null)
                return raiz.izquierdo;

            raiz.valor = MinValor(raiz.derecho);
            raiz.derecho = EliminarRecursivo(raiz.derecho, raiz.valor);
        }

        return raiz;
    }

    private int MinValor(Nodo raiz)
    {
        int minValue = raiz.valor;
        while (raiz.izquierdo != null)
        {
            minValue = raiz.izquierdo.valor;
            raiz = raiz.izquierdo;
        }
        return minValue;
    }
}

class Program
{
    static void Main()
    {
        ArbolBinario arbol = new ArbolBinario();
        int opcion;
        do
        {
            Console.WriteLine("\nMenú:");
            Console.WriteLine("1. Insertar un nodo");
            Console.WriteLine("2. Recorrido en Inorden");
            Console.WriteLine("3. Recorrido en Preorden");
            Console.WriteLine("4. Recorrido en Postorden");
            Console.WriteLine("5. Buscar un valor");
            Console.WriteLine("6. Eliminar un nodo");
            Console.WriteLine("7. Salir");
            Console.Write("Elige una opción: ");
            opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    Console.Write("Introduce un valor para insertar: ");
                    int valorInsertar = int.Parse(Console.ReadLine());
                    arbol.Insertar(valorInsertar);
                    break;

                case 2:
                    Console.WriteLine("Recorrido en Inorden:");
                    arbol.RecorridoInorden();
                    break;

                case 3:
                    Console.WriteLine("Recorrido en Preorden:");
                    arbol.RecorridoPreorden();
                    break;

                case 4:
                    Console.WriteLine("Recorrido en Postorden:");
                    arbol.RecorridoPostorden();
                    break;

                case 5:
                    Console.Write("Introduce el valor a buscar: ");
                    int valorBuscar = int.Parse(Console.ReadLine());
                    bool encontrado = arbol.Buscar(valorBuscar);
                    if (encontrado)
                        Console.WriteLine($"Valor {valorBuscar} encontrado.");
                    else
                        Console.WriteLine($"Valor {valorBuscar} no encontrado.");
                    break;

                case 6:
                    Console.Write("Introduce el valor a eliminar: ");
                    int valorEliminar = int.Parse(Console.ReadLine());
                    arbol.Eliminar(valorEliminar);
                    break;

                case 7:
                    Console.WriteLine("Saliendo...");
                    break;

                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }
        } while (opcion != 7);
    }
}

import sys
import activity_1
import activity_2



def actividad_3():
    print("Ejecutando actividad 3...")

def main(args):
    if len(args) > 1:
        if args[1] == "1":
            activity_1.continuos_sine()
            activity_1.discrete_sine()
        elif args[1] == "2":
            activity_2.saludo()
        elif args[1] == "3":
            actividad_3()
        else:
            print(f"Actividad desconocida: {args[1]}")
    else:
        print("Uso: python archivo.py [act_1 | act_2 | act_3]")

if __name__ == "__main__":
    main(sys.argv)
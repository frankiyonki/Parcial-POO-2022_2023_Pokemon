# Parcial-POO-2022_2023_Pokemon
'''
link al repositorio:https://github.com/frankiyonki/Parcial-POO-2022_2023_Pokemon.git
Ejercicio 1 (5 puntos) 

Pokémon, qué empezó originalmente como un videojuego, gracias a su elevada popularidad logró expandirse a otros medios de entretenimiento como ha sido series de televisión, películas e incluso juegos de cartas.

 En este ejercicio vamos a centrarnos únicamente en la versión de videojuego y vamos a intentar recrear un elemento muy importante de él. Vamos a crear una criatura Pokémon. Estas criaturas son como guerreros combatientes, los cuáles están guiados, entrenados y liderados por su entrenador.

 

Para quien no esté muy familiarizado con este videojuego, y por añadir un poco más de contexto, cada entrenador va a tener a su cargo un conjunto de criaturas Pokémon, los cuáles les va a servir al entrenador para cuándo él quiera entrar en combate con otro entrenador. Sin embargo, cuando dos entrenadores entran en combate, solamente las criaturas Pokémon son las que compiten entre sí.

 

En este ejercicio, vamos a hacer una versión programada en Python para que dos jugadores puedan jugar a este juego. Los jugadores se encontrarán representados por los entrenadores de cada uno de los equipos.

 

No es necesario implementar el docString correspondiente a las funciones y métodos desarrollados, aunque se recomienda hacer el diagrama de flujo de los métodos en papel de forma previa a su resolución.

 

En base a estas especificaciones se solicita que programe la clase Pokémon:

 

Cada criatura Pokémon va a estar caracterizado por:     

o   ID del Pokémon. Número entero y único que identifica a la criatura Pokémon.

o   Nombre del Pokémon. Nombre de la critarua Pokémon.

o   Tipo de arma que lleva a cabo el Pokémon. En esta primera versión del juego, solamente 4 tipos de arma van a existir: Puñetazo, Patada, Codazo, Cabezazo.

o   Puntos de salud que tiene el Pokémon. Deben de estar entre 1 y 100.

o   Índice de ataque del Pokémon. Deben de estar entre 1 y 10.

o   Índice de defensa del Pokémon. Deben de estar entre 1 y 10.

 

Nota: Es obligatorio el uso de enumerados para el atributo del tipo de arma. El índice de ataque del Pokémon se recomienda que contenga el valor del tipo de arma. Se recuerda que el enumerado en Python tiene el formato "Clave / Valor".

 

Se pide:

        i.     Incluya los atributos de esta clase y establezca la visibilidad adecuada (público, privado, protegido). Añada cualquier atributo y/o método que considere necesario.

       ii.     Programe un método constructor que reciba los datos necesarios para crear un Pokémon. El método debe verificar el tipo y valor de cada uno de los parámetros y lanzar la excepción correspondiente cuando no se cumplan los requisitos. El método constructor debe asegurarse de que el atributo ID es una identificación nueva no tomada por otros Pokémons. Así mismo, programe también un método destructor que se encarge de eliminar la instancia de Pokemon de la variable lista de IDs global.

      iii.     Programe un método que mejor corresponda para imprimir objetos de tipo Pokemon según el siguiente ejemplo: “Pokemon ID 8 with name Bulbasaur has as weapon PUNCH and health 87.”

     iv.     Programe los métodos setters y getters para la clase en función de lo que necesite. Si no necesita algún o ningún getter y/o setter, argumente por qué en un comentario dentro del módulo.

      v.     Programe el método is_alive(self) de la clase Pokémon. Este método sirve para saber si el Pokemon está vivo.

     vi.     Programe el método fight_attack(self, Pokémon pokemon_to_attack). Método que implementa el ataque del Pokémon usando un golpe sobre otro Pokémon. Este método se basa en el método fight_defense(self, int points_of_damage) del Pokémon atacado. Se aplicará el índice de ataque del Pokémon atacante como representación del golpe dado. Este método devolverá un booleano True si se ha podido atacar a la criatura Pokémon.

    vii.     Programe el método fight_defense(self, int points_of_damage). Este método implementa la defensa del Pokémon de un golpe de otro Pokémon. Este método actualiza el atributo de puntos de salud que tiene el Pokémon en base a los puntos de daño recibidos menos el índice de defensa del propio Pokémon. Si el índice de defensa es mayor que los puntos de ataque recibidos, el método devolverá false y el Pokémon no sufrirá ningún daño. Este método devolverá un booleano True si se ha sufrido un ataque por parte de otra criatura Pokémon.

   viii.     Pruebe los objetos de la clase Pokémon con los casos de prueba que se le han pasado.

 

 

Para ayudar en el desarrollo de este ejercicio, se le hace entrega de un UML parcialmente completo de la posible implementación de este juego. Se puede modificar o realizar un UML completamente distinto, el cuál es necesario explicar brevemente en un documento de texto o en los comentarios de un fichero .py. En caso de realizar un UML diferente, no se aplicarán los criterios en base a los casos de prueba facilitados, que es probable que no funcionen sin una adaptación previa.

 

Se facilitan también los archivos vacíos dónde deberán estar implementadas las clases que se piden y que tienen que ser completadas por el alumno. En dichas clases, están ya añadidos los casos de prueba de cada una de ellas.

 


Ejercicio 2 (2,5 puntos) Tiempo estimado: 20 minutos.

 

Se propone una extensión del juego propuesto en el ejercicio 4 en la que, en vez de jugar con un solo tipo de Pokémon, se pueda jugar con 4 tipos de Pokémon diferentes: Tierra, Agua, Aire y Electricidad.

 

En base a estas especificaciones en este ejercicio se solicita que:

 

a)    Programe una clase que implemente un Pokémon de Tierra (Earth Pokemon).

·        Este Pokemon va a tener un índice de defensa que va a estar entre 11 y 20.

b)    Programe una clase que implemente un Pokémon de Agua (Water Pokemon).

·        Este Pokemon va a tener un índice de ataque que va a estar entre 11 y 20.

c)     Programe una clase que implemente un Pokémon de Aire (Air Pokemon).

·        Este Pokemon tiene el método fight_defense modificado de tal forma que existe un 50% de posibilidad de que no le afecte un ataque. Este 50% se puede calcular utilizando el módulo random.

d)    Programe una clase que implemente un Pokémon de Electricidad (Electric Pokemon).

·        Este Pokemon tiene el método fight_attack modificado de tal forma que existe un 50% de posibilidad de que su ataque valga el doble de lo originalmente expuesto. Este 50% se puede calcular utilizando el módulo random.

 

 

Reutilice tanto código como sea posible del ejercicio 4 para hacer esta extensión del juego.

 

No es necesario implementar el docString correspondiente a las funciones y métodos desarrollados, aunque se recomienda hacerlo para facilitar la comprensión por parte del estudiante.


Ejercicio 3 (2,5 puntos) Tiempo estimado: 20 minutos.

 

En este último ejercicio se pide que se implemente el módulo principal del juego. Este módulo principal va a implementar la partida que van a jugar los jugadores, los cuales se encuentran identificados como los entrenadores de los combatientes.

 

En este módulo main, lo primero que se hace es obtener la configuración deseada de los Pokemons por parte de cada entrenador. Hay que tener en cuenta, que cada entrenador solamente va a tener tres Pokémons al iniciar la partida.

 

Las características de cada uno de los grupos de Pokemons que va a poseer cada entrenador van a ser introducidas a través de archivos CSV. Los dos archivos CSV a utilizar por en este ejercicio han sido proporcionados:

 

coach_1_pokemons.csv
coach_2_pokemons.csv
 

Se deben crear los Pokémons leyendo los ficheros CSV para cada uno de los entrenadores (ver Flowchart).

 

Seguidamente, una vez que se tienen las configuraciones de cada uno de los equipos, cuya implementación debe realizarse en la función get_data_from_user(), el combate puede comenzar entre los entrenadores.

 

Los combates entre Pokemons se van a realizar secuencialmente. Además, un combate se entiende como aquel llevado a cabo por un Pokémon de cada uno de los equipos. Por lo tanto, en cada turno un Pokémon de uno de los equipos va a atacar a otro Pokémon del otro equipo. Una vez que dos Pokémons entran en combate, no se para este combate hasta que uno de los dos Pokémons es derrotado, momento en el que el siguiente Pokémon del entrenador debe entrar al combate seleccionando un Pokémon de aquellos que no estén derrotados. La función get_pokemon_in_a_list_of_pokemons() tiene que ser implementada para ayudar a que el usuario del juego pueda elegir algún Pokemon que todavía esté sin derrotar por parte de cada uno de los entrenadores. Implementar también la función coach_is_undefeated() para que esta función nos devuelva si todos los Pokémons de un entrenador han sido derrotados o queda alguno vivo.

 

Cuando uno de los dos entrenadores tenga ya todos sus Pokémon derrotados al acabar el turno, se acaba el juego, y se indica no solo quién es el ganador, sino también las estadísticas de cada equipo en base a los puntos de vida de los Pokémons. En el caso de que los dos acaben sin Pokémons en el mismo turno, el juego indicará un empate. En cada turno los dos Pokémons atacan con independencia de si en ese mismo turno es derrotado.

 

Recuerde utilizar las clases implementadas tanto en el ejercicio 4 como en el ejercicio 5 para implementar todos los componentes de este juego.
'''

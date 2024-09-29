import pygame
import random
import sys
"""
dodaj menu liste wynikow itp
spr by kawałki shapow opadaly
i wszystko do sterowania na androidzie
"""
# Definicja kolorow
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127,127,127)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
# Ksztalty tetrisa (SHAPES)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

BRICK_SIZE = 30  # Rozmiar pojedynczego kwadratu

class Grid:
    def __init__(self, width, height):
        """Inicjalizacja siatki."""
        self.width = width
        self.height = height
        # Tworzenie pustej siatki (2D), gdzie 0 oznacza puste pole
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def clear(self):
        """Czyszczenie siatki."""
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def is_row_full(self, row):
        """Sprawdza, czy dany wiersz jest pelny."""
        return all(cell == 1 for cell in row)

    def clear_full_rows(self):
        """Usuwa pelne wiersze i przesuwa pozostale w dol."""
        new_grid = [row for row in self.grid if not self.is_row_full(row)]
        while len(new_grid) < self.height:
            new_grid.insert(0, [0 for _ in range(self.width)])
        self.grid = new_grid

    def can_place_shape(self, shape, position):
        """Sprawdza, czy dany ksztalt moze byc umieszczony w siatce bez kolizji."""
        shape_height = len(shape)
        shape_width = len(shape[0])
        x_start, y_start = position

        for y in range(shape_height):
            for x in range(shape_width):
                if shape[y][x] == 1:
                    # Sprawdza, czy ksztalt wychodzi poza granice planszy lub koliduje z innymi klockami
                    if (x_start + x < 0 or 
                        x_start + x >= self.width or
                        y_start + y >= self.height or
                        self.grid[y_start + y][x_start + x] == 1):
                        return False
        return True

    def place_shape(self, shape, position):
        """Umieszcza ksztalt na planszy."""
        shape_height = len(shape)
        shape_width = len(shape[0])
        x_start, y_start = position

        for y in range(shape_height):
            for x in range(shape_width):
                if shape[y][x] == 1:
                    self.grid[y_start + y][x_start + x] = 1  # Ustawia wartosc 1 tam, gdzie jest klocek

    def draw(self, surface):
        """Rysuje siatke na podanej powierzchni."""
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:  # Rysuje klocek, jesli znajduje sie w danym miejscu
                    pygame.draw.rect(
                        surface, BLUE,
                        (x * BRICK_SIZE, y * BRICK_SIZE, BRICK_SIZE, BRICK_SIZE)
                    )
                # Rysowanie linii siatki
                pygame.draw.rect(
                    surface, WHITE,
                    (x * BRICK_SIZE, y * BRICK_SIZE, BRICK_SIZE, BRICK_SIZE), 1
                )

class Board:
    def __init__(self, width, height):
        """Inicjalizacja planszy."""
        self.grid = Grid(width, height)  # Plansza oparta na siatce
        self.current_shape = None  # Aktualny ksztalt
        self.current_position = (0, 0)  # Pozycja ksztaltu
        self.game_over = False  # Flaga informujaca o koncu gry
        self.spawn_shape()  # Tworzenie nowego ksztaltu

    def spawn_shape(self):
        """Generuje nowy ksztalt i ustawia jego pozycje startowa."""
        self.current_shape = random.choice(SHAPES)  # Losowy ksztalt
        self.current_position = (self.grid.width // 2 - len(self.current_shape[0]) // 2, 0)  # Startowa pozycja
        # Sprawdzanie, czy nowy kształt koliduje z istniejącymi blokami na górze planszy
        if not self.grid.can_place_shape(self.current_shape, self.current_position):
            self.game_over = True  # Jesli kolizja, ustaw game_over na True

    def update(self):
        """Aktualizuje stan planszy, przesuwajac ksztalt w dol."""
        if self.game_over:
            return  # Jeśli gra jest zakończona, nic nie rób

        new_position = (self.current_position[0], self.current_position[1] + 1)  # Nowa pozycja po przesunieciu w dol
        if self.grid.can_place_shape(self.current_shape, new_position):  # Sprawdza kolizje
            self.current_position = new_position  # Przesuwa ksztalt w dol, jesli nie ma kolizji
        else:
            # Ksztalt osiadl - dodaje ksztalt do planszy i czysci pelne wiersze
            self.grid.place_shape(self.current_shape, self.current_position)
            self.grid.clear_full_rows()
            self.spawn_shape()  # Spawnuje nowy ksztalt

    def draw(self, surface):
        """Rysuje plansze na podanej powierzchni."""
        self.grid.draw(surface)  # Rysuje siatke z klockami
        shape_height = len(self.current_shape)
        shape_width = len(self.current_shape[0])
        for y in range(shape_height):
            for x in range(shape_width):
                if self.current_shape[y][x] == 1:  # Rysowanie aktualnego ksztaltu na planszy
                    pygame.draw.rect(
                        surface, BLUE,
                        ((self.current_position[0] + x) * BRICK_SIZE, 
                         (self.current_position[1] + y) * BRICK_SIZE, 
                         BRICK_SIZE, BRICK_SIZE)
                    )
    def move_left(self):
        """Przesuwa ksztalt w lewo, jesli to mozliwe."""
        new_position = (self.current_position[0] - 1, self.current_position[1])  # Nowa pozycja po przesunięciu w lewo
        if self.grid.can_place_shape(self.current_shape, new_position):  # Sprawdza, czy nowa pozycja jest mozliwa
            self.current_position = new_position  # Przesuwa ksztalt w lewo
    def move_right(self):
        """Przesuwa ksztalt w prawo, jesli to mozliwe."""
        new_position = (self.current_position[0] + 1, self.current_position[1])  # Nowa pozycja po przesunięciu w prawo
        if self.grid.can_place_shape(self.current_shape, new_position):  # Sprawdza, czy nowa pozycja jest mozliwa
            self.current_position = new_position  # Przesuwa ksztalt w lewo
    def drop_shape(self):
        """Przesuwa ksztalt w dol do najnizszej mozliwej pozycji."""
        new_position = (self.current_position[0], self.current_position[1])  # Zainicjalizuj nową pozycję

        while self.grid.can_place_shape(self.current_shape, new_position):  # Kontynuuj przesuwanie w dół
            new_position = (new_position[0], new_position[1] + 1)  # Zwiększ wysokość
    
        # Przypisujemy nową pozycję do current_position
        self.current_position = (new_position[0], new_position[1] - 1)  # Przesuń kształt do ostatniej legalnej pozycji
        self.grid.place_shape(self.current_shape, self.current_position)  # Umieść kształt w siatce
        self.grid.clear_full_rows()  # Sprawdź pełne wiersze
        self.spawn_shape()
    def rotate_shape(self):
            """Obraca aktualny ksztalt o 90 stopni w prawo."""
            new_shape = [list(row) for row in zip(*self.current_shape[::-1])]
            if self.grid.can_place_shape(new_shape, self.current_position):
                self.current_shape = new_shape  # Ustawia nowy kształt, jeśli nie ma kolizji    

class Game:
    def __init__(self, width, height):
        """Inicjalizacja gry."""
        pygame.init()
        # Ustawienie rozmiaru ekranu na podstawie siatki (liczba kolumn i wierszy razy rozmiar jednego pola)
        self.screen = pygame.display.set_mode((width * BRICK_SIZE, height * BRICK_SIZE))
        self.clock = pygame.time.Clock()  # Kontrolowanie czasu gry
        self.board = Board(width, height)  # Tworzenie planszy gry
        self.running = True  # Flaga kontrolujaca stan gry
        font_size = int(height * BRICK_SIZE * 0.05)
        self.font = pygame.font.Font(None, font_size)
        self.screen_width, self.screen_height = self.screen.get_size()
    def show_game_over_message(self):
        text = "Przegrales"
        label = self.font.render(text, True, WHITE)  # Renderuje tekst
        label_rect = label.get_rect(center=(self.screen_width // 2, self.screen_height // 2))  # Ustawia etykietę na środku
        self.screen.blit(label, label_rect)  # Rysuje etykietę na ekranie

    def run(self):
        """Glowna petla gry."""
        while self.running:
            # Obsluga zdarzen (np. wyjscie z gry)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # Lewy klawisz
                        self.board.move_left()
                    elif event.key == pygame.K_RIGHT:  # Prawy klawisz
                        self.board.move_right()
                    elif event.key == pygame.K_DOWN:  # Dolny klawisz (przyspieszenie)
                        self.board.drop_shape()
                    elif event.key == pygame.K_UP:  # Gorny klawisz (obrot)
                        self.board.rotate_shape()
            if self.board.game_over:
                self.screen.fill(GREY)
                self.show_game_over_message()
            else:
                # Aktualizacja stanu gry (przesuwanie klockow i kolizje)
                self.board.update()
                # Czyszczenie ekranu
                self.screen.fill(GREY)
                # Rysowanie planszy i aktualnego ksztaltu
                self.board.draw(self.screen)
            # Odswiezanie ekranu
            pygame.display.flip()
            # Ograniczenie do 10 klatek na sekunde
            self.clock.tick(5)

        pygame.quit()

# Przyklad uzycia gry
if __name__ == "__main__":
    game = Game(width=10, height=20)  # Inicjalizacja gry z plansza 10x20
    game.run()  # Uruchomienie glownej petli gry

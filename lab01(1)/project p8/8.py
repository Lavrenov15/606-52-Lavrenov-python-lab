import flet as ft

class Player:
    """Класс для игроков"""
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.moves = ""
    
    def add_move(self, position):
        self.moves += str(position)
    
    def check_win(self):
        win_combinations = [
            "123", "456", "789",
            "147", "258", "369",
            "159", "357"
        ]
        
        for combo in win_combinations:
            if all(pos in self.moves for pos in combo):
                return True
        return False

class TicTacToe:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Крестики-нолики"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        
        self.player_x = Player('x', 'Крестики')
        self.player_o = Player('o', 'Нолики')
        self.current_player = self.player_x
        
        self.available_positions = list(range(1, 10))
        self.buttons = {}
        self.game_active = True  
        
        self.create_interface()
    
    def create_interface(self):
        self.title_text = ft.Text(
            "Крестики-нолики",
            size=30,
            weight=ft.FontWeight.BOLD
        )
        
        self.status_text = ft.Text(
            f"Ход: {self.current_player.name} ({self.current_player.symbol.upper()})",
            size=20
        )
        
        self.game_grid = ft.Column(
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        for i in range(3):
            row = ft.Row(spacing=10, alignment=ft.MainAxisAlignment.CENTER)
            for j in range(3):
                position = i * 3 + j + 1
                button = ft.ElevatedButton(
                    content=ft.Text("", size=40, weight=ft.FontWeight.BOLD),
                    on_click=lambda e, pos=position: self.make_move(pos),
                    width=100,
                    height=100
                )
                self.buttons[position] = button
                row.controls.append(button)
            self.game_grid.controls.append(row)
        
        self.restart_button = ft.ElevatedButton(
            "Новая игра",
            on_click=self.restart_game
        )
        
        self.page.add(
            ft.Column(
                [
                    ft.Container(height=20),
                    self.title_text,
                    ft.Container(height=10),
                    self.status_text,
                    ft.Container(height=20),
                    self.game_grid,
                    ft.Container(height=20),
                    self.restart_button,
                    ft.Container(height=20)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )
    
    def make_move(self, position):
        if not self.game_active:
            return
        
        if position not in self.available_positions:
            return
        
        self.available_positions.remove(position)
        self.current_player.add_move(position)
        
        button = self.buttons[position]
        button.content = ft.Text(self.current_player.symbol.upper(), size=40, weight=ft.FontWeight.BOLD)
        button.disabled = True
        
        self.page.update()
        
        #победа
        if self.current_player.check_win():
            self.game_active = False
            self.show_result(f"ПОБЕДА! {self.current_player.name} выиграли! 🎉")
            return
        
        #ничья
        if not self.available_positions:
            self.game_active = False
            self.show_result("НИЧЬЯ! 🤝")
            return
        
        self.switch_player()
    
    def show_result(self, message):
        """Показывает результат игры и блокирует поле"""
        self.status_text.value = message
        self.status_text.size = 24
        self.status_text.weight = ft.FontWeight.BOLD
        self.page.update()
    
    def switch_player(self):
        self.current_player = self.player_o if self.current_player == self.player_x else self.player_x
        self.status_text.value = f"Ход: {self.current_player.name} ({self.current_player.symbol.upper()})"
        self.page.update()
    
    def restart_game(self, e=None):
        self.game_active = True
        
        self.player_x.moves = ""
        self.player_o.moves = ""
        self.current_player = self.player_x
        
        self.available_positions = list(range(1, 10))
        
        for button in self.buttons.values():
            button.content = ft.Text("", size=40, weight=ft.FontWeight.BOLD)
            button.disabled = False
        
        self.status_text.value = f"Ход: {self.current_player.name} ({self.current_player.symbol.upper()})"
        self.status_text.size = 20
        self.status_text.weight = ft.FontWeight.NORMAL
        self.page.update()

def main(page: ft.Page):
    page.window_width = 450
    page.window_height = 600
    page.window_resizable = False
    
    game = TicTacToe(page)

ft.app(target=main)
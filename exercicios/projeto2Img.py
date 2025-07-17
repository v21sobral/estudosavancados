from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        # Using AsyncImage to load an image from a URL
        image = AsyncImage(source='https://preview.redd.it/whe8j8cvyzx91.jpg?width=640&crop=smart&auto=webp&s=6188131fe8773a40d6e541e5432341b8c564d3e6', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
        return image

if __name__ == '__main__':
    app = MainApp()
    app.run()
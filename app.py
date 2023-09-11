from shiny import App, render, ui,reactive
import palmerpenguins


penguins = palmerpenguins.load_penguins()
app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!",style="background-color:green; color:white; "),
    
    ui.input_slider("n", "Input the Year:", 2007, 2009, 1000),
    ui.output_text_verbatim("filtered_txt"),
    ui.output_data_frame("grid"),

)

def server(input, output, session):
    @reactive.Calc
    def func1():
        return penguins.loc[( penguins['species'].isin(['Chinstrap','Adelie']) ) & (penguins.year == int(input.n()))]
    
    @output
    @render.text
    def filtered_txt():
        return func1()
    
    @output
    @render.data_frame
    def grid():
        
        return render.DataGrid(
                        func1(),
                        height="100%",
                        width="100%",
        )


app = App(app_ui, server)

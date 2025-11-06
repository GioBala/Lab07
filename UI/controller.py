import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_m(self):
        options = []
        musei=self._model.get_musei()
        options.append(ft.DropdownOption("Nessun filtro"))
        for m in musei:
            options.append(
                ft.DropdownOption(
                    m.nome,
                    ),
                )
        return options

    def popola_dropdown_a(self):
        options = []
        artefatti=self._model.get_epoche()
        options.append(ft.DropdownOption("Nessun filtro"))
        for a in artefatti:
            options.append(ft.DropdownOption(a))
        return options

    # CALLBACKS DROPDOWN
    # TODO
    def callback_m(self,e):
        self.museo_selezionato = self._view.dd_musei.value
        if self.museo_selezionato == "Nessun filtro":
            self.museo_selezionato = None

    def callback_a(self,e):
        self.epoca_selezionata = self._view.dd_epoca.value
        if self.epoca_selezionata == "Nessun filtro":
            self.epoca_selezionata = None

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self,e):
        self._view.lw_artefatti.clean()
        artefatti=self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        if len(artefatti)==0:
            self._view.show_alert("Nessun artefatto trovato")
        else:
            for a in artefatti:
                self._view.lw_artefatti.controls.append(ft.Text(a))
        self._view.update()

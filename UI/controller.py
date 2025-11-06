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

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self,e):
        self.museo_selezionato = self._view.dd_musei.value
        self.epoca_selezionata = self._view.dd_epoca.value
        self._view.lw_artefatti.clean()
        if self.museo_selezionato is None:
            self._view.show_alert("Seleziona un museo")
        if self.epoca_selezionata is None:
            self._view.show_alert("Seleziona un epoca")
        if self.epoca_selezionata is not None and self.epoca_selezionata is not None:
            if self.museo_selezionato == "Nessun filtro":
                self.museo_selezionato = None
            if self.epoca_selezionata == "Nessun filtro":
                self.epoca_selezionata = None
            artefatti=self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
            if len(artefatti)==0:
                self._view.show_alert("Nessun artefatto trovato")
            else:
                for a in artefatti:
                    self._view.lw_artefatti.controls.append(ft.Text(a))
        self._view.update()
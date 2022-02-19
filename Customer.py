class Customer:
    def __init__(self, name, legal_address, actual_address, contract_number, contract_date):
        self.contract_date = contract_date
        self.contract_number = contract_number
        self.actual_address = actual_address
        self.legal_address = legal_address
        self.name = name
        self.departments = []

    class Department:
        def __init__(self, name):
            self.name = name
            self.working_areas = []

        class WorkingArea:
            def __init__(self, number, name):
                self.name = name
                self.number = number
                self.noise_params = 0
                self.weather_conditions = 0

            class NoiseParameter:
                def __init__(self, noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl):
                    self.noise_source = noise_source
                    self.nature_of_noise = nature_of_noise
                    self.sound_lvl = sound_lvl
                    self.max_sound_lvl = max_sound_lvl
                    self.eq_sound_lvl = eq_sound_lvl

            class WeatherCondition:
                def __init__(self, temperature, atmo_pressure, humidity):
                    self.temperature = temperature
                    self.atmo_pressure = atmo_pressure
                    self.humidity = humidity

            def noise_parameter_ini(self, noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl):
                self.noise_params = self.NoiseParameter(noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl)

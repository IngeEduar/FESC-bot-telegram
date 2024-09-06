class Question:
    def __init__(self, id=0, question="", response="", options=None):
        self._id = id
        self._question = question
        self._response = response
        self._options = options if options is not None else []

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_question(self, question):
        self._question = question

    def get_question(self):
        return self._question

    def set_response(self, response):
        self._response = response

    def get_response(self):
        return self._response
    
    def set_options(self, options):
        if options is None or all(isinstance(option, Question) for option in options):
            self._options = options
        else:
            raise ValueError("El argumento debe ser una lista de instancias de Question o None.")
        
    def set_option(self, option):
        self._options.append(option)
    
    def remove_option(self, option):
        self._options.remove(option)

    def get_options(self):
        return self._options
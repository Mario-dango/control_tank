
class PCB_mother:
    def __init__(self, version, revision, contacto_creador="Mario Papetti"):
        self._version = version
        self.revision = revision
        self.contacto_creador = contacto_creador
        
    def cambiar_version(self, nueva_version):
        self.version = nueva_version
        
    def cambiar_revision(self, nueva_revision):
        self.revision = nueva_revision
        
    def cambiar_contacto(self, nuevo_contacto):
        self.version = nuevo_contacto
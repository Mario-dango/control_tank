PROJECT_NAME=cmdCliente

CXX=g++
CXXFLAGS=-Wall -Wextra -std=c++11 -O2
DIR=resourse/lib
XMLRPC= $(DIR)/controllers_h/xmlrpc
PUGIXML= $(DIR)/models_h/pugixml
# Nombre del archivo main
MAIN = main.cpp

INCLUDES=\
	-I. \
	-I.controllers \
	-I.models \
	-I.views \
	-I.$(PUGIXML) \
	-I.$(XMLRPC) \
	-I.$(DIR)/views_h \
	-I.$(DIR)/models_h \
	-I.$(DIR)/controllers_h

SOURCES=\
	main.cpp \
	controllers/archivoController.cpp \
	controllers/xmlrpcController.cpp \
	controllers/mainController.cpp \
	models/archivoModel.cpp \
	views/cmdView.cpp \
	$(PUGIXML)/pugixml.cpp \
	$(XMLRPC)/XmlRpcClient.cpp \
	$(XMLRPC)/XmlRpcServer.cpp \
	$(XMLRPC)/XmlRpcSocket.cpp \
	$(XMLRPC)/XmlRpcUtil.cpp \
	$(XMLRPC)/XmlRpcDispatch.cpp \
	$(XMLRPC)/XmlRpcServerConnection.cpp \
	$(XMLRPC)/XmlRpcServerMethod.cpp \
	$(XMLRPC)/XmlRpcSource.cpp \
	$(XMLRPC)/XmlRpcValue.cpp

HEADERS=\
	$(DIR)/controllers_h/archivoController.hpp \
	$(DIR)/controllers_h/xmlrpcController.hpp \
	$(DIR)/controllers_h/mainController.hpp \
	$(DIR)/models_h/archivoModel.hpp \
	$(DIR)/views_h/cmdView.hpp \
	$(PUGIXML)/pugiconfig.hpp \
	$(PUGIXML)/pugixml.hpp  \
	$(XMLRPC)/base64.h \
	$(XMLRPC)/XmlRpcException.h \
	$(XMLRPC)/XmlRpcClient.h \
	$(XMLRPC)/XmlRpc.h \
	$(XMLRPC)/XmlRpcServer.h \
	$(XMLRPC)/XmlRpcSocket.h \
	$(XMLRPC)/XmlRpcUtil.h \
	$(XMLRPC)/XmlRpcDispatch.h \
	$(XMLRPC)/XmlRpcServerConnection.h \
	$(XMLRPC)/XmlRpcServerMethod.h \
	$(XMLRPC)/XmlRpcSource.h \
	$(XMLRPC)/XmlRpcValue.h


TARGET=$(PROJECT_NAME)

SRCDIRS=\
	controllers \
	models \
	views \
	$(PUGIXML) \
	$(XMLRPC)

OBJDIR=obj

# Recorroo los directorios
SRCS = $(foreach dir,$(SRCDIRS),$(wildcard $(dir)/*.cpp))
OBJS = $(patsubst %.cpp,$(OBJDIR)/%.o,$(notdir $(SRCS)))

$(TARGET): $(OBJS)
	@echo Compilando $<
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(OBJS) $(MAIN) -o $(TARGET)

$(OBJDIR)/%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

$(OBJDIR)/%.o: controllers/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

$(OBJDIR)/%.o: models/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

$(OBJDIR)/%.o: views/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

$(OBJDIR)/%.o: $(PUGIXML)/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

$(OBJDIR)/%.o: $(XMLRPC)/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

.PHONY: clean

clean:
	rm -f $(OBJS) $(TARGET)

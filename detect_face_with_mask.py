# importe a biblioteca opencv
import cv2

#importação do tensorflow


#variável com definição de modelo

# defina um objeto de captura de vídeo
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()


    # Altere o dado de entrada:

    # 2. Converta a imagem em um array Numpy e aumente a dimensão

    ##test_image = np.array(img, dtype=np.float32)
    ##test_image = np.expand_dims(test_image, axis=0)



    # 3. Normalize a imagem

    # Preveja o resultado
    
  
    # Exiba o quadro resultante
    cv2.imshow('quadro', frame)
      
    # Saia da tela com a barra de espaço
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as janelas
cv2.destroyAllWindows()
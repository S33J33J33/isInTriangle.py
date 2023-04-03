def product2(x1 ,y1 ,z1 ,x2 ,y2 ,z2 ,x3 ,y3 ,z3):
    return (y2 - y1) * (z3 - z1) - (y3 - y1) * (z2 - z1) - (x2 - x1) * (z3 - z1) + (x3 - x1) * (z2 - z1) + (x2 - x1) * (
            y3 - y1) - (x3 - x1) * (y2 - y1)

def isInTriangle2(x_t_1 ,y_t_1 ,z_t_1 ,x_t_2 ,y_t_2 ,z_t_2 ,x_t_3 ,y_t_3 ,z_t_3 ,x_o ,y_o ,z_o):
  if product2(x_t_1 ,y_t_1 ,z_t_1 ,x_t_2 ,y_t_2 ,z_t_2 ,x_t_3 ,y_t_3 ,z_t_3) < 0:
      return isInTriangle2(x_t_1 ,y_t_1 ,z_t_1 ,x_t_3 ,y_t_3 ,z_t_3 ,x_t_2 ,y_t_2 ,z_t_2 ,x_o ,y_o ,z_o)
  if product2(x_t_1 ,y_t_1 ,z_t_1 ,x_t_2 ,y_t_2 ,z_t_2 ,x_o ,y_o ,z_o) > 0 and product2(x_t_2 ,y_t_2 ,z_t_2 ,x_t_3 ,
                                                                                        y_t_3 ,z_t_3 ,x_o ,
                                                                                        y_o ,z_o) > 0 and product2(
      x_t_3 ,y_t_3 ,z_t_3 ,x_t_1 ,y_t_1 ,z_t_1 ,x_o ,y_o ,z_o) > 0:
      return True
  return False

if __name__ == '__main__':
  x_triangular_a = 0.1
  y_triangular_a = 0.1 / np.sqrt(3)
  z_triangular_a = 242.0
  x_triangular_b = 0
  y_triangular_b = -0.2 / np.sqrt(3)
  z_triangular_b = 242.0
  x_triangular_o = 0.0
  y_triangular_o = 0.0
  z_triangular_o = 142.0
  
  x_process_cross = 0.0024273504273504276
  y_process_cross = 0.0
  z_process_cross = 145.64102564102564
  
  print(isInTriangle2(x_triangular_o ,y_triangular_o ,z_triangular_o ,x_triangular_a ,y_triangular_a ,z_triangular_a ,
                        x_triangular_b ,y_triangular_b ,z_triangular_b ,x_process_cross ,y_process_cross ,
                        z_process_cross))

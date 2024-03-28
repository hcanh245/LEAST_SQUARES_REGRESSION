def solve_equation(a1, b1, c1, a2, b2, c2):
    Det = a1*b2 - a2*b1
    Dx = c1*b2 - c2*b1
    Dy = a1*c2 - a2*c1
    x = round(Dx/Det, 4)
    y = round(Dy/Det, 4)
    return x, y

def solve_3_equations(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    # Tính định thức của ma trận hệ số của các biến
    det_A = a1 * b2 * c3 + b1 * c2 * a3 + c1 * a2 * b3 - a1 * c2 * b3 - b1 * a2 * c3 - c1 * b2 * a3
    # Tính định thức của ma trận khi thay cột của biến x bằng cột của các số hạng tự do
    det_x = d1 * b2 * c3 + b1 * c2 * d3 + c1 * d2 * b3 - d1 * c2 * b3 - b1 * d2 * c3 - c1 * b2 * d3
    # Tính định thức của ma trận khi thay cột của biến y bằng cột của các số hạng tự do
    det_y = a1 * d2 * c3 + d1 * c2 * a3 + c1 * a2 * d3 - a1 * c2 * d3 - d1 * a2 * c3 - c1 * d2 * a3
    # Tính định thức của ma trận khi thay cột của biến z bằng cột của các số hạng tự do
    det_z = a1 * b2 * d3 + b1 * d2 * a3 + d1 * a2 * b3 - a1 * d2 * b3 - b1 * a2 * d3 - d1 * b2 * a3
    # Tính nghiệm
    x = round(det_x/det_A, 4)
    y = round(det_y/det_A, 4)
    z = round(det_z/det_A, 4)
    return x, y, z
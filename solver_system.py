"""
Solver Sistem Persamaan Nonlinear
NIM: 21120123140117
NIMx = 17 mod 4 = 1
Kombinasi: g1A dan g2B

Sistem Persamaan:
f1(x,y) = x² + xy - 10 = 0
f2(x,y) = y + 3xy² - 57 = 0

Solusi sejati: x = 2, y = 3
"""

import math

# ==================== FUNGSI DASAR ====================
def f1(x, y):
    """f1(x,y) = x² + xy - 10"""
    return x**2 + x*y - 10

def f2(x, y):
    """f2(x,y) = y + 3xy² - 57"""
    return y + 3*x*y**2 - 57

# ==================== FUNGSI ITERASI ====================
# Fungsi g1A dan g2A (Halaman 5 - Divergen)
def g1A(x, y):
    """g1A: x = (10 - x²)/y"""
    return (10 - x**2) / y

def g2A(x, y):
    """g2A: y = 57 - 3xy²"""
    return 57 - 3*x*y**2

# Fungsi g1B dan g2B (Halaman 6 - Konvergen)
def g1B(x, y):
    """g1B: x = √(10 - xy)"""
    return math.sqrt(10 - x*y)

def g2B(x, y):
    """g2B: y = √((57-y)/(3x))"""
    return math.sqrt((57 - y) / (3*x))

# ==================== TURUNAN UNTUK NEWTON-RAPHSON ====================
def df1_dx(x, y):
    """∂f1/∂x = 2x + y"""
    return 2*x + y

def df1_dy(x, y):
    """∂f1/∂y = x"""
    return x

def df2_dx(x, y):
    """∂f2/∂x = 3y²"""
    return 3*y**2

def df2_dy(x, y):
    """∂f2/∂y = 1 + 6xy"""
    return 1 + 6*x*y

# ==================== METODE ITERASI TITIK TETAP - JACOBI ====================
def iterasi_jacobi(g1, g2, x0, y0, epsilon=1e-6, max_iter=100):
    """
    Metode Iterasi Jacobi:
    x(r+1) = g1(x(r), y(r))
    y(r+1) = g2(x(r), y(r))
    """
    print("\n" + "="*80)
    print("METODE ITERASI TITIK TETAP - JACOBI")
    print("="*80)
    print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    print("-"*80)
    
    x, y = x0, y0
    print(f"{0:<6} {x:<12.6f} {y:<12.6f} {0:<12.6f} {0:<12.6f}")
    
    for i in range(1, max_iter + 1):
        try:
            x_new = g1(x, y)
            y_new = g2(x, y)
            
            if not (math.isfinite(x_new) and math.isfinite(y_new)):
                print(f"\nDIVERGEN pada iterasi {i} (nilai tidak terdefinisi)")
                return None, None, False, i
            
            delta_x = abs(x_new - x)
            delta_y = abs(y_new - y)
            
            print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {delta_x:<12.6f} {delta_y:<12.6f}")
            
            if abs(x_new) > 1e10 or abs(y_new) > 1e10:
                print(f"\nDIVERGEN pada iterasi {i} (nilai terlalu besar)")
                return None, None, False, i
            
            if delta_x < epsilon and delta_y < epsilon:
                print(f"\nKONVERGEN pada iterasi {i}")
                print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
                print(f"Verifikasi: f1 = {f1(x_new, y_new):.6e}, f2 = {f2(x_new, y_new):.6e}")
                return x_new, y_new, True, i
            
            x, y = x_new, y_new
            
        except Exception as e:
            print(f"\nERROR pada iterasi {i}: {str(e)}")
            return None, None, False, i
    
    print(f"\nTidak konvergen setelah {max_iter} iterasi")
    return x, y, False, max_iter

# ==================== METODE ITERASI TITIK TETAP - SEIDEL ====================
def iterasi_seidel(g1, g2, x0, y0, epsilon=1e-6, max_iter=100):
    """
    Metode Iterasi Seidel (Gauss-Seidel):
    x(r+1) = g1(x(r), y(r))
    y(r+1) = g2(x(r+1), y(r))  <- menggunakan x(r+1) yang baru
    """
    print("\n" + "="*80)
    print("METODE ITERASI TITIK TETAP - SEIDEL (GAUSS-SEIDEL)")
    print("="*80)
    print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    print("-"*80)
    
    x, y = x0, y0
    print(f"{0:<6} {x:<12.6f} {y:<12.6f} {0:<12.6f} {0:<12.6f}")
    
    for i in range(1, max_iter + 1):
        try:
            x_new = g1(x, y)
            
            if not math.isfinite(x_new):
                print(f"\nDIVERGEN pada iterasi {i} (x tidak terdefinisi)")
                return None, None, False, i
            
            y_new = g2(x_new, y)  # Menggunakan x_new
            
            if not math.isfinite(y_new):
                print(f"\nDIVERGEN pada iterasi {i} (y tidak terdefinisi)")
                return None, None, False, i
            
            delta_x = abs(x_new - x)
            delta_y = abs(y_new - y)
            
            print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {delta_x:<12.6f} {delta_y:<12.6f}")
            
            if abs(x_new) > 1e10 or abs(y_new) > 1e10:
                print(f"\nDIVERGEN pada iterasi {i} (nilai terlalu besar)")
                return None, None, False, i
            
            if delta_x < epsilon and delta_y < epsilon:
                print(f"\nKONVERGEN pada iterasi {i}")
                print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
                print(f"Verifikasi: f1 = {f1(x_new, y_new):.6e}, f2 = {f2(x_new, y_new):.6e}")
                return x_new, y_new, True, i
            
            x, y = x_new, y_new
            
        except Exception as e:
            print(f"\nERROR pada iterasi {i}: {str(e)}")
            return None, None, False, i
    
    print(f"\nTidak konvergen setelah {max_iter} iterasi")
    return x, y, False, max_iter

# ==================== METODE NEWTON-RAPHSON ====================
def newton_raphson(x0, y0, epsilon=1e-6, max_iter=100):
    """
    Metode Newton-Raphson untuk sistem persamaan nonlinear
    """
    print("\n" + "="*80)
    print("METODE NEWTON-RAPHSON")
    print("="*80)
    print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    print("-"*80)
    
    x, y = x0, y0
    print(f"{0:<6} {x:<12.6f} {y:<12.6f} {0:<12.6f} {0:<12.6f}")
    
    for i in range(1, max_iter + 1):
        u = f1(x, y)
        v = f2(x, y)
        
        # Hitung turunan parsial
        du_dx = df1_dx(x, y)
        du_dy = df1_dy(x, y)
        dv_dx = df2_dx(x, y)
        dv_dy = df2_dy(x, y)
        
        # Determinan Jacobi
        det = du_dx * dv_dy - du_dy * dv_dx
        
        if abs(det) < 1e-10:
            print(f"\nDeterminan Jacobi mendekati nol pada iterasi {i}")
            return None, None, False, i
        
        # Update x dan y
        x_new = x - (u * dv_dy - v * du_dy) / det
        y_new = y + (u * dv_dx - v * du_dx) / det
        
        delta_x = abs(x_new - x)
        delta_y = abs(y_new - y)
        
        print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {delta_x:<12.6f} {delta_y:<12.6f}")
        
        if delta_x < epsilon and delta_y < epsilon:
            print(f"\nKONVERGEN pada iterasi {i}")
            print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
            print(f"Verifikasi: f1 = {f1(x_new, y_new):.6e}, f2 = {f2(x_new, y_new):.6e}")
            return x_new, y_new, True, i
        
        x, y = x_new, y_new
    
    print(f"\nTidak konvergen setelah {max_iter} iterasi")
    return x, y, False, max_iter

# ==================== METODE SECANT ====================
def secant_method(x0, y0, x1, y1, epsilon=1e-6, max_iter=100):
    """
    Metode Secant untuk sistem persamaan nonlinear
    Menggunakan aproksimasi turunan dengan beda hingga
    """
    print("\n" + "="*80)
    print("METODE SECANT")
    print("="*80)
    print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
    print("-"*80)
    
    x_prev, y_prev = x0, y0
    x, y = x1, y1
    
    print(f"{0:<6} {x_prev:<12.6f} {y_prev:<12.6f} {0:<12.6f} {0:<12.6f}")
    print(f"{1:<6} {x:<12.6f} {y:<12.6f} {abs(x-x_prev):<12.6f} {abs(y-y_prev):<12.6f}")
    
    for i in range(2, max_iter + 1):
        u = f1(x, y)
        v = f2(x, y)
        u_prev = f1(x_prev, y_prev)
        v_prev = f2(x_prev, y_prev)
        
        # Aproksimasi turunan parsial dengan beda hingga
        dx = x - x_prev
        dy = y - y_prev
        
        if abs(dx) < 1e-10 and abs(dy) < 1e-10:
            print(f"\nPerubahan terlalu kecil pada iterasi {i}")
            return None, None, False, i
        
        # Aproksimasi Jacobian
        du_dx = (u - u_prev) / dx if abs(dx) > 1e-10 else df1_dx(x, y)
        du_dy = (f1(x, y+0.0001) - u) / 0.0001
        dv_dx = (v - v_prev) / dx if abs(dx) > 1e-10 else df2_dx(x, y)
        dv_dy = (f2(x, y+0.0001) - v) / 0.0001
        
        det = du_dx * dv_dy - du_dy * dv_dx
        
        if abs(det) < 1e-10:
            print(f"\nDeterminan Jacobi mendekati nol pada iterasi {i}")
            return None, None, False, i
        
        # Update
        x_new = x - (u * dv_dy - v * du_dy) / det
        y_new = y + (u * dv_dx - v * du_dx) / det
        
        delta_x = abs(x_new - x)
        delta_y = abs(y_new - y)
        
        print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {delta_x:<12.6f} {delta_y:<12.6f}")
        
        if delta_x < epsilon and delta_y < epsilon:
            print(f"\nKONVERGEN pada iterasi {i}")
            print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
            print(f"Verifikasi: f1 = {f1(x_new, y_new):.6e}, f2 = {f2(x_new, y_new):.6e}")
            return x_new, y_new, True, i
        
        x_prev, y_prev = x, y
        x, y = x_new, y_new
    
    print(f"\nTidak konvergen setelah {max_iter} iterasi")
    return x, y, False, max_iter

# ==================== MAIN PROGRAM ====================
def main():
    print("="*80)
    print("PENYELESAIAN SISTEM PERSAMAAN NONLINEAR")
    print("="*80)
    print("NIM: 21120123140117")
    print("NIMx = 17 mod 4 = 1")
    print("Kombinasi Fungsi Iterasi: g1A dan g2B")
    print("\nSistem Persamaan:")
    print("f1(x,y) = x² + xy - 10 = 0")
    print("f2(x,y) = y + 3xy² - 57 = 0")
    print("\nSolusi Sejati: x = 2, y = 3")
    print("="*80)
    
    # Parameter
    x0, y0 = 1.5, 3.5
    epsilon = 1e-6
    max_iter = 100
    
    print(f"\nTebakan Awal: x0 = {x0}, y0 = {y0}")
    print(f"Toleransi (epsilon) = {epsilon}")
    print(f"Maksimum Iterasi = {max_iter}")
    
    # Ringkasan hasil
    results = []
    
    # 1. Iterasi Jacobi dengan g1A dan g2B
    print("\n" + "█"*80)
    print("1. ITERASI TITIK TETAP - JACOBI (g1A dan g2B)")
    print("█"*80)
    x, y, conv, iter_count = iterasi_jacobi(g1A, g2B, x0, y0, epsilon, max_iter)
    results.append(("Jacobi (g1A, g2B)", x, y, conv, iter_count))
    
    # 2. Iterasi Seidel dengan g1A dan g2B
    print("\n" + "█"*80)
    print("2. ITERASI TITIK TETAP - SEIDEL (g1A dan g2B)")
    print("█"*80)
    x, y, conv, iter_count = iterasi_seidel(g1A, g2B, x0, y0, epsilon, max_iter)
    results.append(("Seidel (g1A, g2B)", x, y, conv, iter_count))
    
    # 3. Newton-Raphson
    print("\n" + "█"*80)
    print("3. METODE NEWTON-RAPHSON")
    print("█"*80)
    x, y, conv, iter_count = newton_raphson(x0, y0, epsilon, max_iter)
    results.append(("Newton-Raphson", x, y, conv, iter_count))
    
    # 4. Secant
    print("\n" + "█"*80)
    print("4. METODE SECANT")
    print("█"*80)
    x1, y1 = 1.4, 3.6  # Tebakan kedua untuk metode Secant
    x, y, conv, iter_count = secant_method(x0, y0, x1, y1, epsilon, max_iter)
    results.append(("Secant", x, y, conv, iter_count))
    
    # Ringkasan
    print("\n" + "="*80)
    print("RINGKASAN HASIL")
    print("="*80)
    print(f"{'Metode':<25} {'x':<12} {'y':<12} {'Status':<12} {'Iterasi':<10}")
    print("-"*80)
    
    for method, x_val, y_val, converged, iters in results:
        status = "Konvergen" if converged else "Divergen"
        x_str = f"{x_val:.6f}" if x_val is not None else "N/A"
        y_str = f"{y_val:.6f}" if y_val is not None else "N/A"
        print(f"{method:<25} {x_str:<12} {y_str:<12} {status:<12} {iters:<10}")
    
    print("="*80)
    
    # Analisis Konvergensi
    print("\nANALISIS KONVERGENSI:")
    print("-" * 80)
    print("1. Iterasi Jacobi (g1A, g2B):")
    print("   - Kombinasi ini menggabungkan g1A dari halaman 5 (divergen)")
    print("     dengan g2B dari halaman 6 (konvergen)")
    print("   - Hasil: Kemungkinan divergen karena g1A tidak stabil")
    print()
    print("2. Iterasi Seidel (g1A, g2B):")
    print("   - Menggunakan nilai x baru untuk menghitung y")
    print("   - Lebih cepat konvergen dibanding Jacobi jika konvergen")
    print()
    print("3. Newton-Raphson:")
    print("   - Metode paling cepat konvergen (kuadratik)")
    print("   - Memerlukan perhitungan turunan parsial")
    print()
    print("4. Metode Secant:")
    print("   - Aproksimasi Newton-Raphson tanpa turunan eksplisit")
    print("   - Kecepatan konvergensi antara titik tetap dan Newton-Raphson")
    print("="*80)

if __name__ == "__main__":
    main()
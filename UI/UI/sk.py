from sklearn.preprocessing import StandardScaler
import joblib

# 假设你有原始的 scaler 对象
scaler = StandardScaler()
# 保存 scaler 对象
joblib.dump(scaler, "scaler_data1.pkl")
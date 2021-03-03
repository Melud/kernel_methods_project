import read_write
import kernels
import methods#.methods as methods


def main():
	for i in range(3):
		X_train = read_write.read_X100(f"data/Xtr{i}_mat100.csv")
		y_train = read_write.read_labels(f"data/Ytr{i}.csv")
		X_test = read_write.read_X100(f"data/Xte{i}_mat100.csv")

		linear_kernel = kernels.Linear()
		# gaussian_kernel = kernels.Gaussian()
		svm = methods.SVM(linear_kernel, reg_val=1e-1)
		# = methods.KernelLogisticRegression(linear_kernel, reg_val=1e-3)
		svm.learn(X_train, y_train)
		y_pred = svm.predict(X_train)
		print(methods.accuracy(y_train, y_pred))
		y_test = svm.predict(X_test)
		# print(y_test)
		read_write.write(y_test,
		                 "predictions/Yte.csv",
		                 offset=i*1000,
		                 append=(i != 0))


if __name__ == '__main__':
	main()

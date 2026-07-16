import joblib
import sys
from evaluate import evaluate_model

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_evaluate.py <mode>")
        print("<mode> should be either 'dev' or 'test'")
        sys.exit(1)
    mode = sys.argv[1]
    if mode not in ["dev", "test"]:
        print("Invalid mode. Choose 'dev' or 'test'.")
        sys.exit(1)

    evaluate_model(mode)

if __name__ == "__main__":
    main()
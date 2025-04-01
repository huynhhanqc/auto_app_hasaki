import pandas as pd
import logging
import os

logging = logging.getLogger(__name__)

class ExcelHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File Excel không tồn tại: {self.file_path}")

    def read_test_data(self, selected_tcid=None):
        try:
            df = pd.read_excel(self.file_path)
            if selected_tcid:
                df = df[df['TC_ID'] == selected_tcid]
            if df.empty:
                raise ValueError(f"Không tìm thấy TC_ID: {selected_tcid}")
            return [
                (row['TC_ID'], row['Description'], row['Steps'], row['Expected Result'])
                for _, row in df.iterrows()
            ]
        except Exception as e:
            logging.error(f"Lỗi khi đọc file Excel {self.file_path}: {e}")
            raise

    def update_test_result(self, tc_id, status):
        try:
            df = pd.read_excel(self.file_path)
            if 'Status' not in df.columns:
                df['Status'] = ""
            df['Status'] = df['Status'].fillna("")
            df['Status'] = df['Status'].astype(str)
            if tc_id not in df['TC_ID'].values:
                logging.warning(f"Không tìm thấy TC_ID {tc_id} trong file Excel.")
                return
            df.loc[df['TC_ID'] == tc_id, 'Status'] = status
            df.to_excel(self.file_path, index=False)
            logging.info(f"Updated status for TC_ID {tc_id}: {status} in {self.file_path}")
        except Exception as e:
            logging.error(f"Lỗi khi ghi file Excel {self.file_path}: {e}")
            raise
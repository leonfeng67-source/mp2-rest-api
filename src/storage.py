import logging

logger = logging.getLogger(__name__)


class DatasetStorage:
    def __init__(self):
        self._store = {}
        self._counter = 0

    def save(self, df, filename):
        """Store a copy of the data and return a new integer ID."""
        self._counter += 1
        dataset_id = self._counter
        self._store[dataset_id] = {"filename": filename, "df": df.copy()}
        logger.debug("Stored dataset: id=%d, rows=%d", dataset_id, len(df))
        return dataset_id

    def get(self, dataset_id):
        """Return a copy of the stored DataFrame, or None."""
        entry = self._store.get(dataset_id)
        if entry is None:
            logger.debug("Dataset not found in storage: id=%s", dataset_id)
            return None
        df = entry["df"].copy()
        logger.debug("Retrieved dataset copy: id=%d, rows=%d", dataset_id, len(df))
        return df

    def get_metadata(self, dataset_id):
        """Return the dataset metadata, or None."""
        entry = self._store.get(dataset_id)
        if entry is None:
            logger.debug("Metadata requested for missing dataset: id=%s", dataset_id)
            return None
        df = entry["df"]
        metadata = {
            "id": dataset_id,
            "filename": entry["filename"],
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": [str(c) for c in df.columns],
        }
        logger.debug("Retrieved metadata: id=%d", dataset_id)
        return metadata

    def update(self, dataset_id, df):
        """Replace an existing dataset; return True, or False if missing."""
        entry = self._store.get(dataset_id)
        if entry is None:
            logger.debug("Update failed, dataset missing: id=%s", dataset_id)
            return False
        entry["df"] = df.copy()
        logger.debug("Updated dataset: id=%d, rows=%d", dataset_id, len(df))
        return True

    def clear(self):
        """Clear all data and reset the ID counter."""
        self._store.clear()
        self._counter = 0
        logger.debug("Cleared all datasets")

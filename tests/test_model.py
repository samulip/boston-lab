import numpy as np

from boston.model import get_boston_df

def test_get_boston_df():
    df = get_boston_df()
    assert df.shape == (506, 14)
    assert (df.dtypes == np.float64).all()

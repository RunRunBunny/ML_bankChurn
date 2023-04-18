{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "855a1595",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi.testclient import TestClient\n",
    "\n",
    "from app import app, predict_bankChurn\n",
    "from userInfo import userInfo\n",
    "\n",
    "client = TestClient(app)\n",
    "\n",
    "def test_input_data(mocker):\n",
    "    data = {\n",
    "        \"creditscore\": 0,\n",
    "        \"age\": 0,\n",
    "        \"tenure\": 0,\n",
    "        \"balance\": 0,\n",
    "        \"numofproducts\": 0,\n",
    "        \"estimatedsalary\": 0,\n",
    "        \"geography_Germany\": 0,\n",
    "        \"geography_Spain\": 0,\n",
    "        \"gender_Male\": 0,\n",
    "        \"hascrcard\": 0,\n",
    "        \"isactivemember\": 0\n",
    "    }\n",
    "\n",
    "    response = client.post(\"/predict\", json = data)\n",
    "\n",
    "    assert response.status_code == 200\n",
    "    assert \"predictions\" in response.json()\n",
    "    assert isinstance(response.json()[\"predictions\"], list)\n",
    "    assert len(response.json()[\"predictions\"]) == 1\n",
    "    assert isinstance(response.json()[\"predictions\"][0], float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bb4f78c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import { useNotification } from "./useNotification";

const usePYModels = () => {
  const { NotificationHandler } = useNotification();

  const predictpetclassifyhub = async (images) => {
    console.log(images);
    if (images.length == 0) {
      return [];
    }
    try {
      const data = new FormData();
      const files = [];
      for (let i = 0; i < images.length; i++) {
        data.append("file", images[i].file);
        files.push(images[i].file.name);
      }
      const response = await fetch(
        "http://localhost:8501/predictpetclassifyhub",
        {
          method: "POST",
          body: data,
        }
      );
      const resData = await response.json();
      if (resData.status == resData.status) {
        NotificationHandler(resData.title, resData.message, resData.status);
      }
      const responseData = resData.about.split(",");
      var predictionArray = images;
      for (var i = 0; i < predictionArray.length; i++) {
        predictionArray[i]["prediction"] = responseData[i];
      }
      return predictionArray;
    } catch (error) {
      console.log(error.message);
      NotificationHandler("Error", "Predictions failed to work.", "Error");
      const about = [];
      return about;
    }
  };
  return { predictpetclassifyhub };
};
export default usePYModels;

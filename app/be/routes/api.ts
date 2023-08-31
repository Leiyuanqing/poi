/* eslint-disable @typescript-eslint/no-var-requires */
/* eslint-disable no-var */
import { Router, Request, Response } from "express";
import { fstat } from "fs";

// Export the router
const router = Router();

let getprice: any;
var fs = require('fs');
fs.readFile('demofile/poi.json', (err: any, data: { toString: () => any; })=>{
  if (err){
    console.log(err);
  }
  else{
    console.log(data, data.toString());
    const pricestr = data.toString();
    getprice = JSON.parse(pricestr);
    console.log(getprice)
  }
})

let getheatmap: any;
var fs = require('fs');
fs.readFile('demofile/poi.json', (err: any, data: { toString: () => any; })=>{
  if (err){
    console.log(err);
  }
  else{
    console.log(data, data.toString());
    const heatmapstr = data.toString();
    getheatmap = JSON.parse(heatmapstr);
    console.log(getheatmap)
  }
})

// TODO: 通过读取文件，加载预先处理好的房价数据与热力图数据
// 建议使用的库：fs

// 房价接口
router.post("/price", async (req: Request, res: Response) => {
  console.log(req.body);
  // TODO: 获取请求中所携带的小区名信息，从预先处理好的房价数据中找到对应的价格
  var found = false;
  for(const o in getprice){
    if(getprice[o].name == req.body.name){
      found = true;
      const price = {
        price: getprice[o].scores,
      };
      return res.status(200).json(price);
    };
  }
  if(found == false){
    return res.status(404).send({ err: "Not found" });
  }

  /***
  const found = true;
  if (found) {
    const price = {
      price: 12345,
    };
    return res.status(200).json(price);
  } else {
    return res.status(404).send({ err: "Not found" });
  }
  ***/
});

// 热力图接口

router.get("/heatmap", async (req: Request, res: Response) => {
  return res.status(200).json(getheatmap);
});

// Export default.
export default router;

import React, { useEffect } from "react";
import "./App.css";
import AMapLoader from "@amap/amap-jsapi-loader";
import qs from "qs";

const BACKEND_URL =
  process.env.NODE_ENV === "production" ? "" : "http://localhost:30000";

const DEMO_DATA = [
  { lng: 116.191031, lat: 39.988585, count: 10 },
  { lng: 116.389275, lat: 39.925818, count: 11 },
  { lng: 116.287444, lat: 39.810742, count: 12 },
  { lng: 116.481707, lat: 39.940089, count: 13 },
  { lng: 116.410588, lat: 39.880172, count: 14 },
  { lng: 116.394816, lat: 39.91181, count: 15 },
  { lng: 116.416002, lat: 39.952917, count: 16 },
];

function App() {
  // React Hooks 用于创建状态变量与修改状态变量的函数
  // 所有页面显示依赖的变量都必须采用这种方式定义，不能直接定义变量，否则将不起作用
  // React会根据状态变量是否被修改，来决定是否重新渲染页面
  const [xiaoqu, setXiaoqu] = React.useState<string>();
  const [returnValue, setReturnValue] = React.useState<any>();

  // 存储异步加载的高德地图JS脚本
  const [AMap, setAMap] = React.useState<any>();
  // 存储实际显示的地图变量
  const [map, setMap] = React.useState<any>();
  // 存储用于绘制热力图的变量
  // TODO: 通过API从后端拉取热力图相关数据，使用setDataSet接口显示房价热力图数据
  const [heatmap, setHeatmap] = React.useState<any>();

  useEffect(() => {
    // 初始化高德地图组件
    AMapLoader.load({
      // TODO: 替换为你的JS API开发者Key
      key: "6862e9562bd025a69927fe822a228b7b",
      version: "2.0",
      plugins: ["AMap.HeatMap"], // 需要使用的的插件列表，如比例尺'AMap.Scale'等
    })
      .then((AMap) => {
        setAMap(AMap);
        const map = new AMap.Map("container", {
          //设置地图容器id
          viewMode: "2D", //是否为3D地图模式
          zoom: 11, //初始化地图级别
          center: [116.4, 39.9], //初始化地图中心点位置
        });
        map.plugin(["AMap.HeatMap"], async function () {
          // TODO: 调整热力图参数，提升美观性
          //初始化heatmap对象
          const heatmap = new AMap.HeatMap(map, {
            radius: 25, //给定半径
            opacity: [0, 0.8],
            /*,
            gradient:{
                0.5: 'blue',
                0.65: 'rgb(117,211,248)',
                0.7: 'rgb(0, 255, 0)',
                0.9: '#ffea00',
                1.0: 'red'
            }
             */
          });
          // TODO: 从后端拉取数据，设置热力图
          const res = await fetch(`${BACKEND_URL}/api/heatmap`, {
            method: "GET",
            // mode: "no-cors",
            // TODO: 通过正确设置请求头headers中的"Content-Type"的值与请求body，使得后端能够正确收到数据
            headers: {
              "Content-Type": "application/json; charset=UTF-8",
            },
            //body: qs.stringify({name:xiaoqu}),
            //body: JSON.stringify({"name":"东王庄"})
          });
          const data = await res.json();
          console.log(data)
          heatmap.setDataSet({
            data: data,
            max: 20,
          });
          setHeatmap(heatmap);
        });
        setMap(map);
      })
      .catch((e) => {
        console.log(e);
      });
  }, []);

  // => 箭头函数是JS/TS语言中的匿名函数
  const handleChange = (event: any) => {
    // 相关的输出可以在浏览器开发者工具的控制台界面查看
    console.log("表单值修改事件：", event);
    setXiaoqu(event.target.value);
  };

  // TODO: 向后端提交正确的数据，并处理后端回送的响应
  const handleSubmit = async (event: any) => {
    // 阻止表单提交默认的刷新窗口操作
    event.preventDefault();
    console.log("提交表单事件：", event);
    const res = await fetch(`${BACKEND_URL}/api/price`, {
      method: "POST",
      // mode: "no-cors",
      // TODO: 通过正确设置请求头headers中的"Content-Type"的值与请求body，使得后端能够正确收到数据
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
      //body: qs.stringify({name:xiaoqu}),
      body: JSON.stringify({"name": xiaoqu})
      //body: JSON.stringify({"name":"东王庄"})
    });
    // 如果后端设计的返回值为JSON，则通过这种方式获取数据
    const data = await res.json();
    console.log("返回值：", data);
    console.log(data.price);
    setReturnValue(data.price);
  };

  // 采用JSX编写页面
  return (
    <div className="App">
      {/* TODO: 这是一个简单的表单提交，需要修改相关的文字描述以符合任务要求 */}
      <form onSubmit={handleSubmit}>
        <label>
          名字：
          <input type="text" value={xiaoqu} onChange={handleChange} />
        </label>
        <input type="submit" value="查询" />
      </form>
      <br />
      响应数据：{`${returnValue}`}
      {/* 高德地图 */}
      <div
        id="container"
        className="map"
        style={{ height: "700px", width: "100%" }}
      ></div>
    </div>
  );
}

export default App;

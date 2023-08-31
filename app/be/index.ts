import logger from "jet-logger";

import morgan from "morgan";
import helmet from "helmet";
import cors from "cors";

import express from "express";
import "express-async-errors";

import apiRouter from "./routes/api";

// Constants
const app = express();

/***********************************************************************************
 *                                  Middlewares
 **********************************************************************************/

// Common middlewares
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(morgan("dev"));

// Security (helmet recommended in express docs)
if (process.env.NODE_ENV === "production") {
  app.use(helmet());
}

if (process.env.NODE_ENV !== "production") {
  // 在非生产模式下，设置“跨域”白名单
  const whitelist = ["http://localhost:3000"];
  app.use(
    cors({
      origin: function (origin, callback) {
        if (!origin || whitelist.indexOf(origin) !== -1) {
          callback(null, true);
        } else {
          callback(new Error("Not allowed by CORS"));
        }
      },
    })
  );
}

/***********************************************************************************
 *                         API routes and error handling
 **********************************************************************************/

// Add api router
app.use("/api", apiRouter);

// Constants
const serverStartMsg = "Express server started on port: ",
  port = process.env.PORT || 30000;

// Start server
app.listen(port, () => {
  logger.info(serverStartMsg + port);
});

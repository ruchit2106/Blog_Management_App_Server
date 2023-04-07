import express from "express";
import { getPostStats } from "../controllers/admin.js";
import { verifyToken } from "../middleware/auth.js";

const router = express.Router();

/* READ for post analysis*/
router.get("/admin", verifyToken,getPostStats);


/* UPDATE */
// router.patch("/:id/:friendId", verifyToken, addRemoveFriend);

export default router;

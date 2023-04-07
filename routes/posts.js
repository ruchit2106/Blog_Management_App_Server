import express from "express";
import { getFeedPosts, getSearchedPosts, getUserPosts, likePost , commentPost, deletePost /*getPostComments*/} from "../controllers/posts.js";
import { verifyToken } from "../middleware/auth.js";

const router = express.Router();

/* READ */
router.get("/", verifyToken, getFeedPosts);
router.get("/:searchquery", verifyToken, getSearchedPosts);

router.get("/:userId/posts", verifyToken, getUserPosts);
// router.get("/:id/showcomments",verifyToken,getPostComments);

/* UPDATE */
router.patch("/:id/like", verifyToken, likePost);
router.patch("/:id/comment",verifyToken,commentPost);


/* DELETE */
router.delete("/:id",verifyToken,deletePost);

export default router;
